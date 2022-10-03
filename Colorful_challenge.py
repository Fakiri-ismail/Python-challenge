# Minimum Time to Make Rope Colorful
def minCost(colors: str, neededTime) -> int:

    def fun(num_list):
        return sum(num_list) - max(num_list) if len(num_list) > 1 else 0

    min_cost = 0
    color = colors[0]
    successif_color = [neededTime[0]]
    for i in range(1,len(colors)):
        if color == colors[i]:
            successif_color.append(neededTime[i])
        else:
            min_cost += fun(successif_color)
            color = colors[i]
            successif_color = [neededTime[i]]
    min_cost += fun(successif_color)
    return min_cost



if __name__=='__main__':
    colors_1, neededTime_1 = "aabaa", [1,2,3,4,1]
    print(minCost(colors_1, neededTime_1))