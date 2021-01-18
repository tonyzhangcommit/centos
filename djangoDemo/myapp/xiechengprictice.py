# 这里主要为协程练习

def customer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('消费者正在消费 %s' % n)
        r = "200 OK"

def produce(c):
    # 这里接受一个参数，参数类型为一个生成器
    c.send(None)    # 启动生成器
    n = 0
    while n < 10:
        n = n + 1
        print("生产者生产了 %s" %n)
        r = c.send(n)
        print("消费者消费%s" % r)
    c.close()

if __name__ == '__main__':
    def generator_1(titles):
        # yield titles
        for title in titles:
            yield title


    def generator_2(titles):
        yield from titles


    titles = ['Python', 'Java', 'C++']
    for title in generator_1(titles):
        print('生成器1:', title)
    for title in generator_2(titles):
        print('生成器2:', title)