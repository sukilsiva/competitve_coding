class pizza_problem:
    def make_simple(self, number, id):
        array = []
        if id == 2:
            quo = number // 2
            for i in range(0, quo):
                array.append(id)
        if id == 3:
            quo = number // 3
            for i in range(0, quo):
                array.append(id)
        if id == 4:
            quo = number // 4
            for i in range(0, quo):
                array.append(id)
        return array


    def rules_for_explanations(self, explanations, pizza_taken = 0):
        pizza_available = int(explanations[0]) - pizza_taken
        pizza_for_2 = [explanations[1]]
        pizza_for_3 = [explanations [2]]
        pizza_for_4 = [explanations[3]]
        if pizza_for_2[0] > 2:
            pizza_for_2 = self.make_simple(pizza_for_2[0], 2)
        if pizza_for_3[0] > 3:
            pizza_for_3 = self.make_simple(pizza_for_3[0], 3)
        if pizza_for_4[0] > 4:
            pizza_for_4 = self.make_simple(pizza_for_4[0], 4)
        return pizza_available, pizza_for_2, pizza_for_3, pizza_for_4

    

    def track_the_data(self, explanations, pizza_description):
       stack_count = []
       temp = []
       pizza_No = []
       for m, i in enumerate(pizza_description):
           if i in temp:
               for k,n in enumerate(temp):
                   if n==i:
                       stack_count[k] += 1
                       pizza_No.append(m)
           else:
            temp.append(i)
            stack_count.append(1)
            pizza_No.append(m)
       return temp, stack_count, pizza_No
            


    def preprocess_data(self, raw_data):
        explanations = []
        pizza_description = []
        i = 0
        while i < len(raw_data):
            if i == 0:
                data = raw_data[i]
                explanations.append(data)
                i+=1
            else:
                data = raw_data[i]
                data = data[1:]
                pizza_description.append(sorted(data))
                i+=1
        explanations = explanations[0]
        for k, n in enumerate(explanations):
            if k == 1:
                explanations[k] = int(explanations[k]) * 2
            if k == 2:
                explanations[k] = int(explanations[k]) * 3
            if k == 3:
                explanations[k] = int(explanations[k]) * 4
        return explanations, pizza_description



    def make_simple_2(self, pizza_for_2, pizza_for_3, pizza_for_4):
        try:
            temp_2 = pizza_for_2.pop()
        except:
            pass
        try:
            temp_3 = pizza_for_3.pop()
        except:
            pass
        try:
            temp_4 = pizza_for_4.pop()
        except:
            pass

        return temp_2, temp_3, temp_4



    def max_pizzas_deliverable(self, array, n, sum):
        possible_teams = []
        for i in range(0, len(array)):
            for j in range(i+1, len(array)):
                if array[i] + array[j] == sum:
                    possible_teams.append(array[i])
                    possible_teams.append(array[j])
        return possible_teams, len(possible_teams)



    def deliver_the_pizzas(self, explanations, total_stack, stack_count, pizza_no):
        pizza_available, pizza_for_2, pizza_for_3, pizza_for_4 = self.rules_for_explanations(explanations)
        #overcontent = []
        overcontent_no = []
        for i,n in enumerate(stack_count):
            if n > 1:
                #overcontent.append(total_stack[i])
                overcontent_no.append(i)
                pizza_no.pop(i)
                stack_count[i] -= 1
        temp2, temp3, temp4 = self.make_simple_2(pizza_for_2, pizza_for_3, pizza_for_4)
        array = [temp2, temp3, temp4]
        n = len(array)
        max_deliverable_teams, total_teams = self.max_pizzas_deliverable(array, n, pizza_available)
        teams = max_deliverable_teams.copy()
        pizza_delivered_to = 0
        delivered_pizza_no = []
        itr = 0
        itr_1 = 0
        final_pizza_nos = []
        while itr_1 < total_teams:
            pizza_delivered_to = max_deliverable_teams[0]
            max_deliverable_teams.remove(max_deliverable_teams[0])
            while itr<pizza_delivered_to:
                if overcontent_no:
                    delivered_pizza_no.append(overcontent_no.pop())
                    itr += 1
                if pizza_no:
                    delivered_pizza_no.append(pizza_no.pop())
                    itr += 1
            final_pizza_nos.append(sorted(delivered_pizza_no))
            delivered_pizza_no = [] #Backtracking
            itr = 0 #Backtracking
            pizza_available = pizza_available - pizza_delivered_to
            itr_1 += 1 #Incrementing
        return total_teams, teams, final_pizza_nos



    def write_data(self, total_teams, teams, final_pizzas):
        array = []
        array.append([total_teams])
        i = 0
        while i<len(final_pizzas):
            final_pizzas[i].insert(0, teams[i])
            i += 1
        for j in final_pizzas:
            array.append(j)
        file = open("results.txt", "w")
        for i in array:
            for j in i:
                file.write(str(j))
                file.write(' ')
            file.write('\n')
        #return file
        return array



    def get_data(self, dataset):
       input_file = []
       with open(dataset, "r") as data:
           input_file = [line.split() for line in data.readlines()] 
       #return input_file
       explanations, pizza_description = self.preprocess_data(input_file)
       #return explanations, pizza_description
       total_stack_available, stack_count, pizza_no = self.track_the_data(explanations, pizza_description)
       #return total_stack_available, stack_count, pizza_no
       total_teams, teams, final_pizza_nos = self.deliver_the_pizzas(explanations, total_stack_available, stack_count, pizza_no)
       #return total_teams, teams, final_pizza_nos    
       answer_data = self.write_data(total_teams, teams, final_pizza_nos)
       return answer_data


if __name__ == "__main__":
    order = pizza_problem()
    print(order.get_data("a_example"))
