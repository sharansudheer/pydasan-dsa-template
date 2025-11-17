class stack_using_list:
    def __init__(self):
        self.counter=-1
        self.stack_size = 0

    def stack_init(self,size,counter,stack_size):
        the_stack = []
        stack_size = size
        return the_stack, counter
    
    def stack_push(self, item, counter, stack_size, the_stack):

        if counter > stack_size:
            print("Stack Overflow")
        else:
            the_stack.append(item)
        return the_stack
    