#-*-coding:utf-8-*-
from lxml import etree

class GameRecordParser:
    """

    """
    def __init__(self, game_record_file_path):
        """

        Args:
            game_record_file_path:
        """
        self.game_record_file_path = game_record_file_path

        with open(game_record_file_path, encoding="utf-8") as f:
            str_game_record = f.read()
        # 游戏记录文件里，正文每一行都以<br>开头表示加粗
        str_game_record = str_game_record.replace("<br>", "")
        html_dom = etree.HTML(str_game_record)
        self.html_dom = html_dom


    def determine_identity(self):
        """

        Returns:

        """
        pass


    def calculate_damage(self):
        """

        Returns:

        """
        html_dom = self.html_dom

        # 所有的伤害都是以红字（颜色码为#cc0000）标出
        list_player = html_dom.xpath("//body/font[@color=\"#cc0000\"]/font[@color=\"#f6de9c\"]/text()")
        list_damage = html_dom.xpath("//body/font[@color=\"#cc0000\"]/text()")
        assert len(list_player) == len(list_damage)
        list_player_damage = [(list_player[num], list_damage[num]) for num in range(len(list_player))]
        # print(list_player_damage)

        dict_player_damage = {}
        for player, damage in list_player_damage:
            # 红字记录的除了伤害，还记录了“阵亡”、“杀死了”、“，”的内容
            if damage != "，" and damage != "阵亡" and damage != "杀死了" and damage.find("体力上限") == -1:
                try:
                    dict_player_damage[player].append(damage)
                except KeyError:
                    dict_player_damage[player] = [damage]
        print(dict_player_damage)

        dict_player_count_damage = {}
        for player in dict_player_damage:
            count_damage = 0
            for item in dict_player_damage[player]:
                try:
                    count_damage += int(item[(item.find("受到") + 2): item.find("点")])
                except ValueError:
                    count_damage += int(item[(item.find("失去了") + 3): item.find("点体力")])
            dict_player_count_damage[player] = count_damage

        return dict_player_count_damage


    def calculate_card(self):
        """

        Returns:

        """
        html_dom = self.html_dom

        list_elem = html_dom.xpath("//body/font[@color=\"#f6de9c\"]")
        list_sourceline = [elem.sourceline for elem in list_elem]
        dict_sourceline_elem = dict(zip(list_sourceline, list_elem))

        dict_subject_card = {}
        for elem in list_elem:
            list_action = elem.xpath("text()")
            if list_action[0] in ("使用了卡牌", "打出卡牌", "火攻弃置一张卡牌"):
                pass
            elif list_action[0].find("弃置") != -1:
                pass
            # 排除掉“发动武将技能”这种情况，对两个以上的人发动技能的时候索引1的元素为" "
            elif list_action[0] == "对":
                if list_action[1] in ("发动了武将技能",) or list_action == ["对", " ", "发动了武将技能"]:
                    continue
            else:
                continue
            subject = elem.xpath("font[@color=\"#f6de9c\"]/text()")[0]
            list_card = elem.xpath("font[@color=\"#FFFF00\"]/font[@color=\"#FFFF00\"]/text()")
            list_card = [list_card[2 * i][1:] for i in range(len(list_card) // 2)]
            try:
                dict_subject_card[subject].extend(list_card)
            except KeyError:
                dict_subject_card[subject] = list_card

        return dict_subject_card


    def calculate_decision(self):
        """

        Returns:

        """
        pass
  
  
if __name__ == "main":
  pass
