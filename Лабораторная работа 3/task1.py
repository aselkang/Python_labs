def find(goods_list, goods):
    for i in range(len(goods_list)):
        if goods_list[i] == goods:
            return i
    return None

goods_list = ['product0', 'product1', 'aa', 'aa', 'b', 'c', 'd', 'c']
print(find(goods_list, 'c'))
print(find(goods_list, 'e'))