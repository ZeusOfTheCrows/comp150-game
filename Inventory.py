import Player


class Inventory:
    """
    ---------------------------------------------------------------------------
    Contains number of items, max number of items, and functions to
        add to and remove from inventory.
    ---------------------------------------------------------------------------
    """

    size = 30
    items = []

    @staticmethod
    def add_item(item):
        """
        =======================================================================
        Checks if item can be added to dictionary,
            and adds it if there is space.

        :param item: item to be added
        =======================================================================
        """

        if len(Inventory.items) < Inventory.size:
            Inventory.items.append(item)
        else:
            print('Inventory full')

    def remove_item(self, item):  # todo: make static?
        """
        =======================================================================
        Checks if requested item is in inventory, and removes it if possible.

        :param item: item to be removed
        =======================================================================
        """

        if Inventory.items[Inventory.items.index(item)]:
            print('Removed ' + item.name + ' from inventory')
            Inventory.items[Inventory.items.index(item)] = None
        else:
            print('No such item found in inventory')

    def __str__(self):
        # todo: what on earth does this do @powll?
        out = '\t'
        for item in Inventory.items:
            out += '\t' + item.name + ' '
        return out


class Backpack(Inventory):
    """
    ---------------------------------------------------------------------------
    Contains number of items, max number of items, and functions to
        add to backpack and toggle item between equipped and backpack.
    ---------------------------------------------------------------------------
    """

    size = 6
    items_in = 0
    items = []

    @staticmethod
    def add_item(source_inventory):
        """
        =======================================================================
        Checks if item can be added to backpack from specified place,
            and adds it if there is space.

        :param source_inventory: place from which the item will be added
        =======================================================================
        """

        for item in source_inventory.items:
            if item.to_backpack:
                if Backpack.items_in < Backpack.size:
                    # source_inventory.remove_item(item)
                    Backpack.items.append(item)
                    print('Added ' + item.name + ' to backpack successfully')
                    Backpack.items_in += 1
                else:
                    print('Attempted to add '
                          + item.name +
                          ' to backpack but the backpack is full')

    @staticmethod
    def switch_item(item_to_remove, item_to_add):
        # todo: I'm not quite sure what this does @powll
        """
        =======================================================================
        Equips item from backpack, and adds currently equipped item to backpack
        :param item_to_remove:
        :param item_to_add:
        =======================================================================
        """

        if not item_to_add:
            Backpack.items_in -= 1

        index = Backpack.items.index(item_to_remove)
        Player.Player.weaponEquipped = item_to_remove
        Backpack.items[index] = item_to_add

    def empty_backpack(self, source_inventory):
        # todo: @powll what does any of this do‽
        """
        =======================================================================
        Removes all items from backpack.
        :param source_inventory: I'm not quite sure
        =======================================================================
        """

        for item in self.items:
            # source_inventory.add_item(item)
            self.remove_item(item)
        self.items_in = 0
        print('Emptied the backpack')
