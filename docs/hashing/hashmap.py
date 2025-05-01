# Implementation of hashmap Data Structure

from typing import Any
# implementing hash map

class HashMap:
    def __init__(self) -> None:
        self.map: dict[str,Any] =  {}
    
    # add method in hashmap
    # Time complexity : O(1) average and o(N) worst case
    # Lookup and insertion takes place in O(1) but worst case is O(N) dut to hash collisions
    def add(self,key:str,value:Any)-> None:
        try:
            if key in self.map:
                raise KeyError(f' {key} already exists !')
            self.map[key]=value
            print(f' {key} added : {value}')
            
        except KeyError as e :
            print(f'Add error : {e}')
            
    # get method
    # Time complexity :  O(1) average and O(N) worst
    def get(self,key:str)-> Any:
        try:
            return self.map[key]
        except KeyError :
            print(f' {key} not found !')
            return
        
    
    # updating a record
    # Time complexity : o(1) average
    def update(self,key:str,value:Any) -> None:
        try:
            if key not in self.map:
                raise KeyError(f'{key} does not exist')
            self.map[key]=value
            print(f' updated : {key} == {value}')
        except KeyError as e :
            print(f' update error : {e}')
            
    
    # delete method
    # Time complexity : O(1) average
    def delete(self,key:str) -> None:
        try:
            del self.map[key]
            print(f'deleted key : {key}')
            
        except KeyError :
            print(f'{key} not found')
            
    # Display method
    # Time complexity : O(N)
    def display(self):
        if not self.map:
            print('Hashmap is empty')
            return
        
        print('Hashmap content')
        for key,value in self.map.items():
            print(f' {key} == {value}')
        


if __name__=="__main__":
    _map=HashMap()
    _map.add('user1','vivek')
    _map.add('user2','rohit')
    _map.display()
 