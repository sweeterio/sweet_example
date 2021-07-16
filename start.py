from sweet import Autotest


sweet = Autotest('测试计划示例')

sweet.run()  # 如果要启动某几个测试套件，则可以写： sweet.run('baidu', 'echo') 

