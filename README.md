
# Abstract Data Types in Python

Basic Python implementation for several Abstract data types. Just a learning exercise.

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

  - [Array](#array)
  - [Bag (multisets)](#bag-multisets)
  - [Queue](#queue)

## Array

A one-dimensional array is a sequence of items stored in contiguous memory locations. They allow random access to the individual items. They must contain data of the same type and have a fixed size that can't vary during the array lifetime.

This implementation uses a `ctypes.py_object` to store and manage the data. It defines the following operations:

- `array[index]`
- `array[index] = value`
- `array.clear()`
- `len(array)`
- `item in array`

It also supports iteration and reverse iteration.

## Bag (multisets)

A bag, also known as [multiset](https://en.wikipedia.org/wiki/Multiset), is a container like a shopping bag. It's a set-like container that allows multiple instances of a given value. You can use a bag to store a collection of items. Bags restrict access to individual items.

This implementation uses a [`list`](https://docs.python.org/3/library/stdtypes.html#list) to store and manage the data. It defines the following operations:

- `bag.add(item)`
- `bag.remove(item)`
- `bag.pop()`
- `bag.clear()`
- `len(bag)`
- `item in bag`
- `bag.count(item)`

It also supports iteration and reverse iteration.

## Queue

Queues are [collections](https://en.wikipedia.org/wiki/Collection_(abstract_data_type)) of items. You can modify queues by adding items at one end and removing items from the opposite end.

Queues manage their items in a **first in**, **first out** ([FIFO](https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics))) fashion. They work as a pipe where you push in new items at one end of the pipe and pop old items out from the other end. Adding an item to one end of a queue is known as an **enqueue** operation. Removing an item from the other end is called **dequeue**.

This implementation uses a [`collections.deque`](https://docs.python.org/3/library/collections.html?highlight=collections#collections.deque) to store and manage the data. It defines the following operations:

- `queue.enqueue()`
- `queue.dequeue()`
- `queue.remove(item)`
- `queue.is_empty()`
- `queue.front()`
- `len(queue)`
- `item in queue`

It also supports iteration and reverse iteration.

## Stack

A stack is a data structure where access is only at one end of the sequence. New values are pushed onto the stack to add them to the sequence and
popped off the stack to remove them from the sequence. Stacks are used in many algorithms in computer science. They're useful when parsing information. Stacks are called Last In/First Out or LIFO data structures. The last item pushed is the first item popped.

This implementation uses a [`collections.deque`](https://docs.python.org/3/library/collections.html?highlight=collections#collections.deque) to store and manage the data. It defines the following operations:

- `stack.push(item)`
- `stack.pop(item)`
- `stack.top()`
- `stack.is_empty()`
- `len(stack)`
- `item in stack`

It also supports iteration and reverse iteration.

## Authors

- Leodanis Pozo Ramos - [@lpozo](https://www.github.com/lpozo)

## License

[MIT](https://choosealicense.com/licenses/mit/)
