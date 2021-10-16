import argparse
import os
# parser = argparse.ArgumentParser(description='解析命令行参数')# 先不添加参数
# args = parser.parse_args()  # 打印一下所有参数




parser = argparse.ArgumentParser()
'''
argparse.ArgumentParser(prog=None, usage=None, description=None, 
epilog=None, parents=[], formatter_class=argparse.HelpFormatter, 
prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, 
conflict_handler='error', add_help=True, allow_abbrev=True, exit_on_error=True)

prog - 程序的名称（默认值：sys.argv[0]）
usage - 描述程序用途的字符串（默认值：从添加到解析器的参数生成）
description - 在参数帮助文档之前显示的文本（默认值：无）
epilog - 在参数帮助文档之后显示的文本（默认值：无）
parents - 一个 ArgumentParser 对象的列表，它们的参数也应包含在内
formatter_class - 用于自定义帮助文档输出格式的类
prefix_chars - 可选参数的前缀字符集合（默认值： '-'）
fromfile_prefix_chars - 当需要从文件中读取其他参数时，用于标识文件名的前缀字符集合（默认值： None）
argument_default - 参数的全局默认值（默认值： None）
conflict_handler - 解决冲突选项的策略（通常是不必要的）
add_help - 为解析器添加一个 -h/--help 选项（默认值： True）
allow_abbrev - 如果缩写是无歧义的，则允许缩写长选项 （默认值：True）
exit_on_error - 决定当错误发生时是否让 ArgumentParser 附带错误信息退出。 (默认值: True)
'''
parser.add_argument('--echo',type=int,default=100,nargs='?',help='直接答应参数的值')
'''
add_argument(name or flags...[, action][, nargs][, const][, default][, type]
[, choices][, required][, help][, metavar][, dest])
定义单个的命令行参数应当如何解析。每个形参都在下面有它自己更多的描述，有：
name or flags - 一个命名或者一个选项字符串的列表，例如 foo 或 -f, --foo。
action - 当参数在命令行中出现时使用的动作基本类型。
nargs - 命令行参数应当消耗的数目。
const - 被一些 action 和 nargs 选择所需求的常数。
default - 当参数未在命令行中出现并且也不存在于命名空间对象时所产生的值。
type - 命令行参数应当被转换成的类型。
choices - 可用的参数的容器。
required - 此命令行选项是否可省略 （仅选项可用）。
help - 一个此选项作用的简单描述。
metavar - 在使用方法消息中使用的参数值示例。
dest - 被添加到 parse_args() 所返回对象上的属性名。
'''
# 添加一个位置参数，注意必须是--开头，--echo
parser.add_argument('--list', choices=['a', 'b', 'c'], default='a', nargs='?')#参数候选值
'''nargs的作用是用来限定输入这个参数的个数，
默认情况下我们必须输入1个，
使用'?'的话，就是允许不输入或者输入一个。
'+'的话表示是1个或多个，
使用数字或者'*' 就是允许多个参数，此时所有参数将组成一个列表，
就是设为1也就一个列表和默认的情况不一样'''
parser.add_argument('-v1', '--verbose1', help='increase verbosity')
parser.add_argument('-v2', '--verbose2', help='increase verbosity', dest='ver')#dest指定变量名
#选项参数，类似于Linux命令中的参数，-v是短参数，--verbose是长参数
#如果有长参数，取值的时候就是使用长参数的名字取值。只有短参数的情况下才是用短参数的名字取值。
#当然也可以指定一个别的变量名和位置参数相反，选项参数默认是非必须。不输入选项的情况下取到的值是None，
#输入选项但是又没在后面写值而且也没默认值，则会出错。
#如果需要，也可以将选项设置为必须输入。


#选项参数-设为必须
#使用required=True 后，这个选项就不再是可选的了，而是必须输入
# parser.add_argument('-v3','--verbose3',help='increase verbosity',required=True)


"""选项参数-布尔值或固定值
上面使用可选参数的时候，必须在后面给这个参数赋值。
有时候我只需要一个标识而不需要一个确切的值，比如-h 和 --help。
这个可以通过使用action="store_true" 来实现。"""


parser.add_argument('-v4', '--verbose4', help='increase verbosity', action='store_true')

'''此时你带参数运行，取到的值就是True，如果不带参数运行，取到的值就是False
也可以使用action="store_false" ，则正好相反
另外也可以是指定一个常量，类似action='store_const', const="Test" ，
那么没有-v 值是None，有-v 的值就是"Test" ，此时-v后面不能跟值了，如果有则会被当做是位置参数处理。
默认的设置是 action="store'" 存储参数值。'''

'''action关键参数的其他用法-计数和追加
上面的关键参数action是参数值赋予的方式，除了上面的用法，还可以设置为下面的值，一般用的不多
如果是 'count' 表示将参数出现的次数作为参数的值
如果是 'append' 表示将每次出现的该参数后的值都存入同一个数组再赋值'''

parser.add_argument('-c', '--count', help='参数值是这个参数出现的次数', action='count')
parser.add_argument('-a', '--append', help='参数是一个列表，每次添加一个元素', action='append')




'''将输出转化为字典
上面的例子中每次打印的都是我们设置过的对象，
可以使用内置函数，将参数和值转化为字典的形式 print(vars(args))
'''









args = parser.parse_args()
args.tmp_para=16
print(args.echo)  # 获取参数，打印出来
print(args.list)
print(args.verbose1)

print(args.ver)
print(args.verbose4)
print(args)  # 看看整个的内容
print(vars(args))
def parse_args():
    # 先实例化
    parser = argparse.ArgumentParser(description='解析命令行参数')
    # 依次添加每一个参数
    parser.add_argument('echo', help='直接打印这个参数的值')
    parser.add_argument('num', help='这是个整数', type=int, default=0, nargs='?')
    parser.add_argument('-v', '--verbose', help='increase verbosity')
    # 最后返回
    return parser.parse_args()
def get_parser():
    # parameter priority: command line > config > default
    parser = argparse.ArgumentParser(
        description='Directed Graph Neural Net for Skeleton Action Recognition') #- help时显示的开始文字
    parser.add_argument('--work-dir',default='./work_dir/temp',help='the work folder for storing results')
    parser.add_argument('--model-saved-name', default='')
    parser.add_argument('--config',default='./config/nturgbd-cross-view/test_bone.yaml',help='path to the configuration file')
    # processor
    parser.add_argument('--phase', default='train', help='must be train or test')
    parser.add_argument('--save-score',type=str,default=False,help='if ture, the classification score will be stored')

    # visulize and debug
    parser.add_argument('--seed', type=int, default=1, help='random seed for pytorch')
    parser.add_argument('--log-interval',type=int,default=100,help='the interval for printing messages (#iteration)')
    parser.add_argument('--save-interval',type=int,default=2,help='the interval for storing models (#iteration)')
    parser.add_argument('--eval-interval',type=int,default=5,help='the interval for evaluating models (#iteration)')
    parser.add_argument('--print-log',type=str,default=True,help='print logging or not')
    parser.add_argument('--show-topk',type=int,default=[1, 5],nargs='+',help='which Top K accuracy will be shown')

    # feeder
    parser.add_argument('--feeder', default='feeder.feeder', help='data loader will be used')
    parser.add_argument('--num-worker',type=int,default=os.cpu_count(),help='the number of worker for data loader')
    parser.add_argument('--train-feeder-args',default=dict(),help='the arguments of data loader for training')
    parser.add_argument('--test-feeder-args',default=dict(),help='the arguments of data loader for test')

    # model
    parser.add_argument('--model', default=None, help='the model will be used')
    parser.add_argument('--model-args',type=dict,default=dict(),help='the arguments of model')
    parser.add_argument('--weights',default=None,help='the weights for network initialization')
    parser.add_argument('--ignore-weights',type=str,default=[],nargs='+',help='the name of weights which will be ignored in the initialization')

    # optim
    parser.add_argument('--base-lr', type=float, default=0.01, help='initial learning rate')
    parser.add_argument('--step',type=int,default=[60, 90],nargs='+',help='the epoch where optimizer reduce the learning rate')
    parser.add_argument('--device',type=int,default=0,nargs='+', #nargs： 设置参数在使用可以提供的个数N   参数的绝对个数（例如：3）?' 0或1个参数 '*' 0或所有参数m'+'所有，并且至少一个参数
     help='the indexes of GPUs for training or testing')
    parser.add_argument('--optimizer', default='SGD', help='type of optimizer')
    parser.add_argument('--nesterov', type=str, default=True, help='use nesterov or not')
    parser.add_argument('--batch-size', type=int, default=32, help='training batch size')
    parser.add_argument('--test-batch-size', type=int, default=32, help='test batch size')
    parser.add_argument('--start-epoch', type=int,default=0,help='start training from which epoch')
    parser.add_argument('--num-epoch',type=int,default=120,help='stop training in which epoch')
    parser.add_argument(  #type：参数类型 默认的参数类型是str类型，如果你的程序需要一个整数或者布尔型参数，你需要设置type=int或type=bool，
        '--weight-decay',
        type=float,     #choices：参数值只能从几个选项里面选择
        default=0.0001,  #help参数的值可以给使用工具的人提供该参数是用来设置什么的说明，对于大型的项目，help参数和很有必要的，不然使用者不太明白每个参数的含义
        help='weight decay for optimizer')#default：没有设置值情况下的默认参数 required: 表示这个参数是否一定需要设置
    parser.add_argument('--freeze-graph-until',type=int,default=10,help='number of epochs before making graphs learnable')

    # parser.add_argument('--only_train_part', default=False)
    # parser.add_argument('--only_train_epoch', default=0)
    # parser.add_argument('--warm_up_epoch', default=0)
    return parser




