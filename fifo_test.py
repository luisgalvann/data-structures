import unittest
from unittest import TestCase
from datetime import datetime
from fifo import FifoClass


class PushTest(TestCase):
    '''push: add an element to the class'''

    def test_element_in_fifo(self):
        instance = FifoClass()
        element = 'element'
        instance.push(element)

        self.assertIn(element, instance)


class PopTest(TestCase):
    '''pop: get and remove the oldest element'''

    def test_removed_element(self):
        instance = FifoClass()
        element = 'element'
        instance.push(element)
        instance.pop()

        self.assertNotIn(element, instance)

    def test_oldest_element(self):
        instance = FifoClass()
        instance.push('first element')
        instance.push('second element')
        instance.push('third element')

        oldest_element = instance.pop()
        self.assertEqual(oldest_element, 'first element')
        oldest_element = instance.pop()
        self.assertEqual(oldest_element, 'second element')
        oldest_element = instance.pop()
        self.assertEqual(oldest_element, 'third element')


class SizeTest(TestCase):
    '''size: get the number of elements'''

    def test_empty_size(self):
        instance = FifoClass()
        size = instance.size()

        self.assertEqual(size, 0)

    def test_regular_size(self):
        instance = FifoClass()
        instance.push(1)
        instance.push(2)
        instance.push(3)
        size = instance.size()

        self.assertEqual(size, 3)

    def test_limit_size(self):
        instance = FifoClass()

        for i in range(1_000_000):
            instance.push(i)

        size = instance.size()

        self.assertEqual(size, 1_000_000)


class TimeTest(TestCase):
    '''addition_time: get the datetime when any element present on the FIFO was added'''

    def test_elements_times(self):
        '''Get the creation datetime of any element using its index'''

        instance = FifoClass()
        start_time = datetime.now()
        instance.push(1)
        instance.push(2)
        instance.push(3)
        end_time = datetime.now()

        first_time = instance.addition_time(0)
        second_time = instance.addition_time(1)
        third_time = instance.addition_time(2)

        self.assertLessEqual(start_time, first_time)
        self.assertLessEqual(first_time, second_time)
        self.assertLessEqual(second_time, third_time)
        self.assertLessEqual(third_time, end_time)

    def test_default_times(self):
        '''If no position is specified by default return last element addition'''

        instance = FifoClass()
        instance.push(1)
        instance.push(2)
        instance.push(3)

        last_time = instance.addition_time(2)
        default_time = instance.addition_time()
        self.assertEqual(default_time, last_time)

        instance.pop()
        default_time = instance.addition_time()
        self.assertEqual(default_time, last_time)

        instance.pop()
        default_time = instance.addition_time()
        self.assertEqual(default_time, last_time)

    def test_out_of_range_time(self):
        '''Check if 'out of range' error raises exception'''

        instance = FifoClass()
        instance.push(1)
        instance.push(2)
        instance.push(3)
        instance.pop()
        instance.pop()
        instance.pop()

        with self.assertRaises(IndexError) as cm:
            instance.pop()
            default_time = instance.addition_time()

        msg = 'pop from empty list'
        self.assertEqual(msg, str(cm.exception))


if __name__ == '__main__':
    unittest.main()
