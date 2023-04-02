# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Use hash table to store contacts
    contacts = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            # Use setdefault to add or update contact
            contacts[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            # Use pop to delete contact if it exists
            contacts.pop(cur_query.number, None)
        else:
            # Use get to find contact by number
            # Set name to None if contact not found
            name = contacts.get(cur_query.number, None)
            if name is not None:
                result.append(name)
            else:
                result.append('not found')
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

