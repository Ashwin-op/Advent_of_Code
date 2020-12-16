import re


with open("input.txt") as fp:
    lines = [i.strip() for i in fp.readlines()]

first_blank, second_blank = [i for i, line in enumerate(lines) if not line]
field_lines = lines[:first_blank]
your_ticket_lines = lines[first_blank + 1: second_blank]
nearby_tickets_lines = lines[second_blank + 1:]

fields = [re.search('([^:]+): (\d+)-(\d+) or (\d+)-(\d+)',
                    line).groups() for line in field_lines]
fields = {name: (int(from1), int(to1), int(from2), int(to2))
          for name, from1, to1, from2, to2 in fields}
your_ticket = list(map(int, your_ticket_lines[1].split(',')))
nearby_tickets = [list(map(int, nearby_tickets_lines[i].split(',')))
                  for i in range(1, len(nearby_tickets_lines))]


valid_tickets, invalid_field_sum = [], 0
for ticket in nearby_tickets:
    valid = True
    for value in ticket:
        if not any(from1 <= value <= to1 or from2 <= value <= to2 for from1, to1, from2, to2 in fields.values()):
            valid = False
            invalid_field_sum += value
    if valid:
        valid_tickets.append(ticket)
print(invalid_field_sum)
