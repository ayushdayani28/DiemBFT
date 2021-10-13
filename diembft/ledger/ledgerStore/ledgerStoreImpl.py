from treelib import Tree


class LedgerStore:

    def __init__(self):
        pass

    def add(self, prev_block_id, block_id, transactions):
        pass

    def delete(self, block_id):
        pass

    def find(self, block_id):
        pass

    def prune(self, block_id):
        pass

    def show(self):
        pass


class LedgerStoreImpl(LedgerStore):

    def __init__(self):
        super().__init__()
        self.tree = Tree()
        self.tree.create_node(100, 100)

    def add(self, prev_block_id, block_id, transactions):
        return self.tree.create_node(tag=block_id, identifier=block_id, parent=prev_block_id, data=transactions)

    def delete(self, block_id):
        return self.tree.remove_node(block_id)

    def find(self, block_id):
        return self.tree.get_node(block_id)

    def prune(self, block_id):

        node = self.tree.get_node(block_id)

        parent_node_id = node.predecessor(self.tree.identifier)

        sibling_nodes = self.tree.children(parent_node_id)

        for n in sibling_nodes:
            if n.identifier != block_id:
                self.tree.remove_node(n.identifier)

    def show(self):
        self.tree.show()

# Testing
# c = LedgerStoreImpl()
#
# c.add(100,1, "Add")
# c.add(100,2, "Add")
# c.add(100,3, "Add")
# c.add(3,4, "Add")
# c.add(3,5, "Add")
# c.add(3,6, "Add")
# c.add(2,7, "Add")
# c.add(2,8, "Add")
#
# c.show()
# c.prune(5)
# c.show()
