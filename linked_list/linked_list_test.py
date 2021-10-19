import unittest
from unittest import TestCase
from linked_list import LinkedList


class SetTest(TestCase):
    ''' Test adding elements to the class '''

    def test_set_head(self):
        instance = LinkedList()
        first_element = 25
        second_element = 'string'
        third_element = [1, 'string', (1, 2)]

        instance.set_head(first_element)
        instance.set_head(second_element)
        instance.set_head(third_element)

        self.assertIn(first_element, instance)
        self.assertIn(second_element, instance)
        self.assertIn(third_element, instance)

    def test_set_tail(self):
        instance = LinkedList()
        first_element = 25
        second_element = 'string'
        third_element = [1, 'string', (1, 2)]

        instance.set_tail(first_element)
        instance.set_tail(second_element)
        instance.set_tail(third_element)

        self.assertIn(first_element, instance)
        self.assertIn(second_element, instance)
        self.assertIn(third_element, instance)

    def test_set_node(self):
        instance = LinkedList()
        first_element = 25
        second_element = 'string'
        third_element = [1, 'string', (1, 2)]

        instance.set_node(0, first_element)
        instance.set_node(1, second_element)
        instance.set_node(2, third_element)

        self.assertIn(first_element, instance)
        self.assertIn(second_element, instance)
        self.assertIn(third_element, instance)


class GetTest(TestCase):
    ''' Test retrieving elements from the class '''

    def test_get_head(self):
        instance = LinkedList()
        first_element = 25
        second_element = 'string'

        instance.set_head(first_element)
        result = instance.get_head()
        self.assertEqual(result, first_element)

        instance.set_head(second_element)
        result = instance.get_head()
        self.assertEqual(result, second_element)

    def test_get_tail(self):
        instance = LinkedList()
        first_element = 25
        second_element = 'string'

        instance.set_tail(first_element)
        result = instance.get_tail()
        self.assertEqual(result, first_element)

        instance.set_tail(second_element)
        result = instance.get_tail()
        self.assertEqual(result, second_element)

    def test_get_node(self):
        instance = LinkedList()
        first_element = 25
        second_element = 'string'
        third_element = [1, 'string', (1, 2)]

        instance.set_node(0, first_element)
        result = instance.get_node(0)
        self.assertEqual(result, first_element)

        instance.set_node(1, second_element)
        result = instance.get_node(1)
        self.assertEqual(result, second_element)

        instance.set_node(0, third_element)
        result = instance.get_node(0)
        self.assertEqual(result, third_element)


class PopTest(TestCase):
    ''' Test retrieving elements from the class '''

    def test_pop_head(self):
        instance = LinkedList()
        first_element = 25
        second_element = 'string'

        instance.set_head(first_element)
        instance.set_head(second_element)

        instance.pop_head()
        self.assertNotIn(second_element, instance)

        instance.pop_head()
        self.assertNotIn(first_element, instance)
        
    def test_pop_tail(self):
        instance = LinkedList()
        first_element = 25
        second_element = 'string'

        instance.set_tail(first_element)
        instance.set_tail(second_element)

        instance.pop_tail()
        self.assertNotIn(second_element, instance)

        instance.pop_tail()
        self.assertNotIn(first_element, instance)

    def test_pop_node(self):
        instance = LinkedList()
        first_element = 25
        second_element = 'string'

        instance.set_node(0, first_element)
        instance.set_node(0, second_element)

        instance.pop_node(1)
        self.assertNotIn(first_element, instance)

        instance.pop_node(0)
        self.assertNotIn(second_element, instance)


class SizeTest(TestCase):
    ''' Test the number of elements in the class '''

    def test_empty_size(self):
        instance = LinkedList()
        size = instance.size

        self.assertEqual(size, 0)

    def test_regular_size(self):
        instance = LinkedList()
        instance.set_head(1)
        instance.set_head(2)
        instance.set_head(3)
        size = instance.size

        self.assertEqual(size, 3)

    def test_limit_size(self):
        instance = LinkedList()

        for i in range(10_000):
            instance.set_tail(i)

        size = instance.size

        self.assertEqual(size, 10_000)


class EmptyTest(TestCase):
    ''' Test «pop from empty list» errors '''

    def test_empty_pop_head_error(self):
        with self.assertRaises(IndexError) as cm:
            instance = LinkedList()
            instance.pop_head()

        msg = "pop from empty list"
        self.assertEqual(msg, str(cm.exception))

    def test_empty_pop_tail_error(self):
        with self.assertRaises(IndexError) as cm:
            instance = LinkedList()
            instance.pop_tail()

        msg = "pop from empty list"
        self.assertEqual(msg, str(cm.exception))

    def test_empty_pop_node_error(self):
        with self.assertRaises(IndexError) as cm:
            instance = LinkedList()
            instance.pop_node(0)

        msg = "pop from empty list"
        self.assertEqual(msg, str(cm.exception))


class OutRangeTest(TestCase):
    ''' Test «index out of range» errors '''

    def test_empty_out_get_node_error(self):
        with self.assertRaises(IndexError) as cm:
            instance = LinkedList()
            instance.get_node(0)

        msg = "index out of range"
        self.assertEqual(msg, str(cm.exception))

    def test_top_out_get_node_error(self):
        with self.assertRaises(IndexError) as cm:
            instance = LinkedList()
            instance.set_head('first element')
            instance.set_head('second element')
            instance.get_node(2)

        msg = "index out of range"
        self.assertEqual(msg, str(cm.exception))

    def test_negative_out_get_node_error(self):
        with self.assertRaises(IndexError) as cm:
            instance = LinkedList()
            instance.set_head('element')
            instance.get_node(-1)

        msg = "index out of range"
        self.assertEqual(msg, str(cm.exception))

    def test_top_out_set_node_error(self):
        with self.assertRaises(IndexError) as cm:
            instance = LinkedList()
            instance.set_node(0, 'element')
            instance.set_node(2, 'element')
            print(instance)

        msg = "index out of range"
        self.assertEqual(msg, str(cm.exception))

    def test_negative_out_set_node_error(self):
        with self.assertRaises(IndexError) as cm:
            instance = LinkedList()
            instance.set_node(0, 'element')
            instance.set_node(-1, 'element')
            print(instance)

        msg = "index out of range"
        self.assertEqual(msg, str(cm.exception))

    def test_top_out_pop_node_error(self):
        with self.assertRaises(IndexError) as cm:
            instance = LinkedList()
            instance.set_node(0, 'element')
            instance.pop_node(1)
            print(instance)

        msg = "index out of range"
        self.assertEqual(msg, str(cm.exception))

    def test_negative_out_pop_node_error(self):
        with self.assertRaises(IndexError) as cm:
            instance = LinkedList()
            instance.set_node(0, 'element')
            instance.pop_node(-1)
            print(instance)

        msg = "index out of range"
        self.assertEqual(msg, str(cm.exception))


if __name__ == '__main__':
    unittest.main()
