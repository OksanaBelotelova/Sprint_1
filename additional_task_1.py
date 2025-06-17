types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}
tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

tickets_by_type = {}


def remove_duplicates(tickets):
    uniq_tickets_list = []
    uniq_tickets = {}

    for key, ticket_list in tickets.items():
        uniq_tickets[key] = []
        for ticket in ticket_list:
            if ticket not in uniq_tickets_list:
                uniq_tickets_list.append(ticket)
                uniq_tickets[key].append(ticket)

    return uniq_tickets


def link_tickets_to_types(types, tickets):

    for key, ticket_list in tickets.items():
        type = types[key]
        tickets_by_type[type] = ticket_list

    return tickets_by_type


uniq_tickets = remove_duplicates(tickets)
tickets_by_type = link_tickets_to_types(types, uniq_tickets)

print(tickets_by_type)
