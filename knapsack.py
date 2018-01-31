# This is a script to practice my python coding
# It solves the knapsack problem by using a greedy algorithm

import pandas as pd
import matplotlib.pyplot as plt


class Item:

    number_of_items = 0

    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
        # Or make a new attribute ratio_value and sort on that?
        # self.ratio = self.value/self.weight

        Item.number_of_items += 1

    def __str__(self):
        return "<{}: {}/{} $/kg>".format(self.name, self.value, self.weight)

    def __lt__(self, other):
        return self.value/self.weight < other.value/other.weight

    @classmethod
    def ret_list(cls, dataframe):
        item_list = []
        for index,row in knapsack_file.iterrows():
            item_list.append(Item(row["name"],row["weight"],row["value"]))
        return item_list


class Knapsack:
    def __init__(self, max_weight):
        self.max_weight = max_weight

    def pack_with_items(self,item_list):
        # Initialise empty dictionary
        self.items = {}
        # Sort the item list by highest value/weight
        item_list.sort(reverse = True)
        smallest_weight = item_list[0].weight
        for i in range(0,len(knapsack_file)):
            smallest_weight = min(smallest_weight,item_list[i].weight)
        counter = 0
        weight_left = self.max_weight
        while weight_left >= smallest_weight:
            self.items[item_list[counter]] = int(weight_left/item_list[counter].weight)
            weight_left -= int(weight_left/item_list[counter].weight)*item_list[counter].weight
            counter += 1
        return self.items

    def plot(self):
        plt.bar(range(len(self.items)),list(self.items.values()))
        plt.xticks(
            range(
                len(self.items)
            ),
            [item.name for item in self.items.keys()]
        )
        plt.show()

    @property
    def total_value(self):
        total_value = 0
        for key, value in self.items.items():
            # Need to get weight by using the key in the item_dict
            total_value += value * key.value
        return total_value

    def empty(self):
        delattr(self, 'items')


knapsack_file = pd.read_csv("knapsack.csv")

item_list = Item.ret_list(knapsack_file)
knack = Knapsack(173)
knack.pack_with_items(item_list)
knack.plot()
print(knack.total_value)
