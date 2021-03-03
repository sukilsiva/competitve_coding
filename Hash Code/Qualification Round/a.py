### This is a Hashcode Problem

class Hashcode:
    def make_dataset(self,explanations, description):
        start = []
        end = []
        time_taken = []
        street_name = []
        length_of_routes = []
        routes = []
        streets = int(explanations[2])
        for n,traversal in enumerate(description):
            if n < streets:
                start.append(int(traversal[0]))
                end.append(int(traversal[1]))
                street_name.append(traversal[2])
                time_taken.append(int(traversal[3]))
            else:
                length_of_routes.append(traversal[0])
                routes.append(traversal[1:])
        return start, end, street_name, time_taken,length_of_routes, routes



    def make_routes(self, start, end):
        array = []
        st = 0
        en = 0
        while st <  len(start) and en < len(end):
            array.append((start[st],end[en]))
            st += 1
            en += 1
        return array



    def preprocess_data(self, raw_data):
        explanations = []
        description = []
        for i,n in enumerate(raw_data):
            if i == 0:
                explanations.append(n)
            else:
                description.append(n)
        return explanations[0], description


    
    def graph(self, routes):
        graph_dict = {}
        for start,end in routes:
            if start in graph_dict:
                graph_dict[start].append(end)
            else:
                graph_dict[start] = [end]
        return graph_dict
    


    def make_simulations(self, explanations, routes_graph, street, start, end, route, time, len_of_route):
        intersection_num = 0
        intersections = []
        simulation_time = explanations[0]
        time = 0
        # For the Intersections
        for i in route:
            for j in range(len(i)-1):
                street_name = i[j]
                for n, k in enumerate(street):
                    if k==street_name:
                        intersection_num = end[n]
                if intersection_num not in intersections:
                    intersections.append(intersection_num)
                else:
                    pass
        incoming_streets_dict = {}
        temp = []
        # for the incoming streets for each intersections
        for incoming_streets, outgoing_streets in routes_graph.items():
            for m in outgoing_streets:
                if m in intersections:
                    temp.append((m,incoming_streets))
        for start, end in temp:
            if start not in incoming_streets_dict:
                incoming_streets_dict[start] = [end]
            else:
                incoming_streets_dict[start].append(end)
        incoming_streets = []
        for i in incoming_streets_dict:
            values = incoming_streets_dict[i]
            incoming_streets.append(len(values))
        # FOr cars 
        name = []
        count = []
        for i in route:
            nam = i[0]
            if nam not in name:
                name.append(nam)
                count.append(1)
            else:
                for n, k in enumerate(name):
                    if k == nam:
                        count[n] += 1
                    else:
                        pass
        return incoming_streets, incoming_streets_dict, intersections, name, count, simulation_time


    def write_data(self, length, intersections, incoming_intersection_roads, final_routes, time):
        array = []
        array.append([length])
        intersections = intersections[::-1]
        incoming_intersection_roads = incoming_intersection_roads[::-1]
        final_routes = final_routes[::-1]
        time = time[::-1]
        i = 0
        while intersections:
            intersection = intersections.pop()
            incoming_road = incoming_intersection_roads.pop()
            array.append([intersection])
            array.append([incoming_road])
            while i < incoming_road:
                value = final_routes.pop()+" "+str(time.pop())
                array.append([value])
                i+=1
            i=0 # Backtracking
        file = open("results.txt", "w")
        for i in array:
            for j in i:
                file.write(str(j))
                #file.write()
            file.write('\n')
        #return file
        return array


    def get_data(self, dataset):
        array = []
        with open(dataset, "r") as data:
            array = [line.split() for line in data.readlines()]
        #return array
        explanation, description = self.preprocess_data(array)
        #return explanation, description
        start, end, street, time, len_of_route, route = self.make_dataset(explanation, description=description)
        #return start, end, street, time, len_of_route, route
        routes = self.make_routes(start, end)
        #return routes
        routes_graph = self.graph(routes)
        #return routes_graph
        incoming_intersection_roads, intersections_dict, intersections, cars_initial_location, number_of_cars, simulation_time =   		self.make_simulations(explanation, routes_graph, street, start, end, route, time, len_of_route)
        #return intersections, incoming_intersection_roads, intersections_dict, cars_initial_location, number_of_cars, simulation_time
        length = len(intersections)
        time = []
        final_routes = []
        final_start = []
        final_end = []
        duplicate = intersections[::-1]
        while duplicate:
            temp_end = duplicate.pop()
            for i in intersections_dict:
                if i==temp_end:
                    while intersections_dict[i]:
                        temp_start = intersections_dict[i].pop()
                        final_start.append(temp_start)
                        final_end.append(temp_end)                    
        s = 0
        while s < len(final_start):
            element = (final_start[s], final_end[s])
            for n,i in enumerate(routes):
                if element==i:
                    final_routes.append(street[n])
            s+=1
        for i in final_routes:
            if i in cars_initial_location:
                for n, k in enumerate(cars_initial_location):
                    if k==i:
                        timee = number_of_cars[n]
                        time.append(timee+1)
            else:
                time.append(1)
        #return length, intersections, incoming_intersection_roads,final_routes,time
        answer = self.write_data(length, intersections, incoming_intersection_roads, final_routes, time)
        return answer



if __name__ == "__main__":
    hash = Hashcode()
    print(hash.get_data("a.txt"))
