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
    # Keep list of all existing (i.e. not deleted yet) contacts
    # Use a dictionary to save time (key is the number)
    contact_dict = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            contact_dict[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            try:
                del contact_dict[cur_query.number]
            except KeyError:
                pass
        else:
            result.append(contact_dict.get(cur_query.number, 'not found'))

    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

