# SanGuoSha_Classifier
预测三国杀主公胜负的机器学习项目
## 数据集
###### 一条记录是一局三国杀游戏。字段（属性）是该局游戏的一些参数，分属于选将、位置、运气和玩家技术和游戏态度这五个方面。大多数属性分为四档，按1-4打分。
#### 一、选将
###### 1、主忠反的耐久。耐久大概包括四个方面：（1）本身血厚或可以回血（兀突骨、董卓、华雄、周泰、华佗等）。（2）可以吸收伤害（曹叡、老诸葛、卧龙诸葛、曹节、董允等）。（3）可以反弹伤害或可以卖血为己方获取收益（嵇康、小乔、大乔、郭嘉、荀彧、曹丕、戏志才等）。（4）技能本身带来的低嘲讽（如伏皇后、邓艾、钟会、孙策、秦宓、蔡文姬）。4分-反弹卖血；3分-血厚，回血，吸收，低嘲讽；2分-和3分类似但是能力欠缺一些，比如血不厚但是有手牌上限，再比如陆逊这种只能免疫乐不思蜀和顺手牵羊的；1分-没有或几乎没有防御技，比如界徐庶这种，荐言用处不很大。
###### 2、主忠反的输出。输出大概包括三个方面：（1）强制输出（马超、陈到、关银屏、徐盛、黄忠、荀彧、何太后等）。（2）多次或多血输出（曹婴、张飞、黄忠、许褚、夏侯渊、张星彩等）。（3）拆牌拿牌输出（张辽、刘封、孙鲁育、步练师等）。4分-大概率（超过75%）输出1血及以上，必然拆牌拿牌2张及以上；3分-较大概率（50%）输出1血及以上，大概率拆牌拿牌2张或以上，必然拆牌拿牌1张；2分-大概率输出0.5-1血，大概率拆拿1牌；1分-没有或几乎任何输出技能。
###### 3、主忠反的控场。控场主要包括两种，一种是制造大量牌差（鲁肃、SP貂蝉、神曹操）或血差（神吕布、神周瑜、群贾诩），另一种是能大量使用延时锦囊（大乔、徐晃）。
###### 4、忠反的辅助。辅助包括三种，给输出（包括给武器，给输出牌等，典型如二张、陈宫、刘协），给防御（包括回血，给防御牌或者让摸牌等，典型如华佗、陆绩），解锦囊（卧龙诸葛、曹仁、司马懿、诸葛瑾、董允等）。
###### 5、武将匹配程度：这个具体情况具体分析。比如刘备-荀彧组合，刘备-SP孙尚香组合，满宠-曹仁组合，戏志才-华佗组合，戏志才-沮授组合，吴国太-孙尚香组合，满宠-SP貂蝉组合，满宠-神吕布组合，太多了。除此以外，还要看主忠反双方的“匹配”程度，我遇到过一次兀突骨反打蔡文姬忠的，算是正中下怀吧。
#### 二、位置
###### 主要分为数学距离和武将分布情况，各占一定比例。这个主要分为忠臣位置和反贼位置。忠臣位置的质量取决于二人和主公的在不考虑坐骑和技能的前提下的“曼哈顿距离”之和，再加上两个忠臣之间的距离。反贼的位置和离主公远近关系不大，相比之下紧凑程度（也就是反贼两两之间的6组曼哈顿距离之和）更为重要。武将分布忌讳高嘲讽武将落单，手短武将被队友包围等，需要具体情况具体打分。
#### 三、运气
###### 牌运和判定运气按0-2进行主观打分，0分表示差，1分表示一般，2分表示好。牌运要综合全局，这个东西特别难具体化，比如游戏开局摸到大量的桃和中后期获得大量桃的效果未必一样，张飞获得大量桃有时候不一定比获得大量杀的效果好。判定运气要视每一次判定生效/失效对主忠反三方的影响而定。二者取平均，或者牌运占60%，判定运占40%。
#### 四、玩家发挥
###### 需要整合玩家每一回合的表现来看，主要考察每一回合是否实现了收益最大化，是否有重大失误等。
#### 五、玩家态度
###### 包括是否频繁托管，是否有意无意拖延时间，是否有队友互杀仇杀或者故意帮助对手的现象，内奸的表现（以忠反均衡，先忠后反为标准线，主忠太厉害的情况除外，否则死忠或者开局跳反都视为游戏态度消极），玩家之间是否发生言语冲突等。-2表示态度极差（上述几项全占，或占了大部分），-1表示态度较差（有上述现象之一），0表示态度一般，1表示态度好。
## 模型
###### 因为数据集还在制作中，在不清楚数据集特性的情况下无法确定模型，但是倾向于树模型。整个模型可能会存在很多问题。比如数据集里属性值的确定，如武将耐久度的打分，我在考虑是不是也用机器学习的方法来打标签或者聚类（比如聚为三类：脆、一般、耐打），现在还不确定这种会不会比主观的人工打分更能逼近现实情况。
