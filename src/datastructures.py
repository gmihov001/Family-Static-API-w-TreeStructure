
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        # example list of members
        self._members = [
            {
                "children": [
                    {
                    "children": [
                        {
                            "first_name": "Jimmy",
                            "id": 5005,
                            "last_name": "Jackson"
                        }
                    ],
                    "first_name": "John",
                    "id": 2002,
                    "last_name": "Jackson",
                    "parent": "Bill"
                    },
                    {
                    "children": [
                        {
                            "first_name": "Tom",
                            "id": 1072,
                            "last_name": "Jackson",
                            "parent": "Tim"
                        },
                        {
                            "first_name": "Sue",
                            "id": 6634,
                            "last_name": "Jackson",
                            "parent": "Tim"
                        },
                        {
                            "first_name": "Kim",
                            "id": 3655,
                            "last_name": "Jackson",
                            "parent": "Tim"
                        }
                    ],
                    "first_name": "Tim",
                    "id": 6298,
                    "last_name": "Jackson",
                    "parent": "Bill"
                    },
                    {
                    "first_name": "Lynn",
                    "id": 2310,
                    "last_name": "Jackson",
                    "parent": "Bill"
                    }
                ],
                "first_name": "Bill",
                "id": 1001,
                "last_name": "Jackson"
            },
            {
                "children": [
                    {
                    "children": [
                        {
                            "first_name": "Tom",
                            "id": 7417,
                            "last_name": "Jackson",
                            "parent": "Simon"
                        },
                        {
                            "first_name": "Jim",
                            "id": 7932,
                            "last_name": "Jackson",
                            "parent": "Simon"
                        }
                    ],
                    "first_name": "Simon",
                    "id": 8195,
                    "last_name": "Jackson",
                    "parent": "Judy"
                    }
                ],
                "first_name": "Judy",
                "id": 9130,
                "last_name": "Jackson"
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(1, 9999)

    # def add_member(self, member):
    #     if 'id' in member:
    #         self._members.append(member)
    #     else:
    #         member['id'] = self._generateId()
    #         self._members.append(member)    
    #     return None

    def add_member(self, member):
        member['id'] = self._generateId()
        member['last_name'] = self.last_name
        if 'parent' in member:
            for grandparent in self._members:
                print("grandparent", grandparent)
                if grandparent['first_name'] == member['parent']:
                    if 'children' in grandparent:
                        grandparent['children'].append(member)
                    else:
                        grandparent['children'] = [member]  
                else:
                    for parent in grandparent['children']:
                        if parent['first_name'] == member['parent']:
                            if 'children' in parent:
                                parent['children'].append(member)
                            else:
                                parent['children'] = [member]            
        else:
            self._members.append(member)

        return None

    def get_all_descendants(self, id):
        for grandparent in self._members:
            if grandparent['id'] == id:
                children = []
                grandchildren = []
                for child in grandparent['children']:
                    children.append(child['first_name'])
                    if 'children' in child:
                        for grandchild in child['children']:
                            grandchildren.append(grandchild['first_name'])   
                return {
                    "children": children,
                    "grandchildren": grandchildren
                }
            else:
                for parent in grandparent['children']:
                    if parent['id'] == id:
                        children = []
                        for child in parent['children']:
                            children.append(child['first_name'])
                        return {
                            "children": children,
                            "grandchildren": "none"
                        }            

    def get_ancestors(self, id):
        for grandparent in self._members:
            for child in grandparent['children']:
                if child['id'] == id:
                    return {"parent": child['parent']}
                else:
                    for grandchild in child['children']:
                        if grandchild['id'] == id:
                            return {
                                'parent': grandchild['parent'],
                                'grandparent': child['parent'] 
                            }    

    def get_siblings(self, id):
        for grandparent in self._members:
            for child in grandparent['children']:
                if child['id'] == id:
                    return {"siblings": [
                        str(child['first_name']) for child in grandparent['children'] if child['id'] != id
                    ]}
                else:
                    for grandchild in child['children']:
                        if grandchild['id'] == id:
                            return {"siblings": [
                                str(grandchild['first_name']) for grandchild in child['children'] if grandchild['id'] != id
                            ]}                      


    def delete_member(self, id):
        # fill this method and update the return
        for position in range(len(self._members)):
            if self._members[position]["id"] == id:
                removed = self._members.pop(position)
                return removed
        
    def get_member(self, id):
        # fill this method and update the return
        for m in self._members:
            if m["id"] == id:
                return m
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members