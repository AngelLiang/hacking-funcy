from .compat import range, Mapping, Set, Sequence, Iterator, Iterable


__all__ = ('isa', 'is_mapping', 'is_set', 'is_seq', 'is_list', 'is_tuple',
           'is_seqcoll', 'is_seqcont',
           'iterable', 'is_iter')


def isa(*types):
    """
    Creates a function checking if its argument
    is of any of given types.
    """
    return lambda x: isinstance(x, types)

is_mapping = isa(Mapping)  # 是否是映射对象
is_set = isa(Set)  # 是否是集合
is_seq = isa(Sequence)  # 是否是序列对象
is_list = isa(list)  # 是否是队列
is_tuple = isa(tuple)  # 是否是元组

is_seqcoll = isa(list, tuple)
is_seqcont = isa(list, tuple, Iterator, range)

iterable = isa(Iterable)
is_iter = isa(Iterator)  # 是否是可迭代对象
