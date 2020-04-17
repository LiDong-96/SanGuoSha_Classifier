# SanGuoSha_Classifier
预测三国杀主公胜负的机器学习项目
## 数据集
###### 一条数据是一局三国杀游戏。属性是该局游戏的一些客观情况，包括选将、位置、运气和玩家技术和态度四个大的方面。选将方面的属性包括主忠反的耐久、输出、控场和爆发能力，忠反的辅助能力，主忠反武将卡牌依赖程度，主忠武将的匹配程度，反贼之间的武将匹配程度等；位置只占一个属性；运气包括牌运和判定运气；玩家技术和态度主要包括主忠反玩家本身的技术，玩家是否有恶意违规现象，玩家游戏态度积极与否，是否长时间托管离开，玩家之间是否爆发言语冲突，内奸的表现等。大多数属性按1-5打分（1分为一格）。下面来具体解释这些属性的细节。
###### 1.主忠反的耐久。耐久我能想到的包括三个方面：本身血厚或可以回血（兀突骨、董卓、华雄、周泰、华佗等），可以吸收伤害（曹叡、老诸葛、卧龙诸葛、曹节、董允等），可以反弹伤害或可以卖血为己方获取收益（嵇康、小乔、大乔、郭嘉、荀彧、曹丕、戏志才等），技能本身带来的低嘲讽（如伏皇后、邓艾、钟会、孙策、秦宓、蔡文姬）。我选几个标将根据耐打程度来试打分：刘备3，关羽1，张飞1，赵云3，孙权2，周瑜2，孙尚香3，郭嘉4，夏侯惇4，曹操3。
###### 2.主忠反的输出。输出我能想到的有三种：强制输出（马超、陈到、关银屏、徐盛、黄忠、荀彧、何太后等）、多次或多血输出（曹婴、张飞、黄忠、许褚、夏侯渊、张星彩等）、拆牌拿牌输出（张辽、刘封、孙鲁育、步练师等）。
###### 3.主忠反的控场。控场主要包括两种，一种是制造大量牌差（鲁肃、SP貂蝉、神曹操）或血差（神吕布、神周瑜、群贾诩），另一种是能大量使用延时锦囊（大乔、徐晃）。
###### 4.主忠反的爆发。爆发不仅仅和将面有关，也要结合具体的游戏局势，比如从将面看SP孙尚香并不属于爆发型武将，但如果装备区牌多，或者手牌有大量装备蓄爆，就是爆发力很强的武将。
###### 5.忠反的辅助。辅助包括三种，给输出（包括给武器，给输出牌等，典型如二张、陈宫、刘协），给防御（包括回血，给防御牌或者让摸牌等，典型如华佗、陆绩），解锦囊（卧龙诸葛、曹仁、司马懿、诸葛瑾、董允等）。
###### 6.主忠反卡牌依赖度。对卡牌依赖程度高低和这个武将耐不耐打并没有必然的联系。武将的卡牌依赖性指的是他（她）的技能效果好坏是否依赖卡牌的质量。输出型武将如黄忠就是卡牌依赖性武将，单体型的钟繇也是卡牌依赖性很强的一位。技能本身和卡牌质量关系不大的武将卡牌依赖性低，比如朱治、曹叡、郭嘉、卑弥呼、蔡夫人等。当然，没有哪个武将是绝对不依赖卡牌的。
###### 7.武将匹配程度：这个具体情况具体分析。比如刘备-荀彧组合，刘备-SP孙尚香组合，满宠-曹仁组合，戏志才-华佗组合，戏志才-沮授组合，吴国太-孙尚香组合，满宠-SP貂蝉组合，满宠-神吕布组合，太多了。除此以外，还要看主忠反双方的“匹配”程度，我遇到过一次兀突骨反打蔡文姬忠的，算是正中下怀吧。
###### 8.位置。主要分为数学距离和武将分布情况，各占一定比例。这个主要分为忠臣位置和反贼位置。忠臣位置的质量取决于二人和主公的在不考虑坐骑和技能的前提下的“曼哈顿距离”之和，再加上两个忠臣之间的距离。反贼的位置和离主公远近关系不大，相比之下紧凑程度（也就是反贼两两之间的6组曼哈顿距离之和）更为重要。武将分布忌讳高嘲讽武将落单，手短武将被队友包围等，需要具体情况具体打分。
###### 9.运气。牌运和判定运气按0-2进行主观打分，0分表示差，1分表示一般，2分表示好。牌运要综合全局，这个东西特别难具体化，比如游戏开局摸到大量的桃和中后期获得大量桃的效果未必一样，张飞获得大量桃有时候不一定比获得大量杀的效果好。判定运气要视每一次判定生效/失效对主忠反三方的影响而定。二者取平均，或者牌运占60%，判定运占40%。
###### 10.玩家技术。需要整合玩家每一回合的表现来看，主要考察每一回合是否实现了收益最大化，是否有重大失误等。
###### 11.玩家态度。分主忠和反贼两个数据项。主要包括是否频繁托管，是否有意无意拖延时间，是否有队友互杀仇杀或者故意帮助对手的现象，内奸的表现（以忠反均衡，先忠后反为标准线，主忠太厉害的情况除外，否则死忠或者开局跳反都视为游戏态度消极），玩家之间是否发生言语冲突等。-2表示态度极差（上述几项全占，或占了大部分），-1表示态度较差（有上述现象之一），0表示态度一般，1表示态度好。
## 模型
###### 暂定为神经网络，但是数据集一开始可能很小，也就几十个数据，后面我会慢慢扩充。考虑到数据集规模，神经网络的层数不可能太多，而且会限制神经元数量。输出层就两个神经元，一个是“主公赢”，一个是“主公输”。我会通过调参让这两个神经元的输出值尽可能为一正一负，值为正的那个就是预测的结果。如果某次预测两个神经元输出值都为正或者负，选择值较大的一种情况。
