def feet_to_steps(user_feet):
    return(int(user_feet/2.5))
   #write your code here

if __name__ == '__main__':
    user_feet = float(input())
    print(feet_to_steps(user_feet))