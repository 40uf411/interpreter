class SyntacticalAnalyser(object):

    rules = {}
    result = []

    data = []

    def __init__(self, rules):
        self.rules = rules

    def check(self,rule, data):
        if self.rules[rule].len != data.__len__():
            return False
        else:
            for count, element in enumerate(self.rules[rule]):
                if element[0] != data[count][0] or (element[1] != "" and element[1] != data[count][1]):
                    return False

            return {
                "type": "full"
            }

    def match(self, data):
        found = False
        exp_next = []
        for rule in self.rules:
            # check if this data matches any rule
            result = self.check(rule, data)

            # if so
            if result:


        # if not return empty arrays and code 0 which means no rule found
        return [[], 0, [], []]

    def parse(self, data, expect_rule = None):

        # temporary elements chain
        temp_chain = []
        expect_next = ()

        for pattern, value in data:
            # testing if we are expecting a certain element/s
            if expect_next is not None:
                # if so then test if the pattern is not correct and the value doesn't match
                for expect in expect_next:
                    if pattern != expect[0] or (expect_next[1] != "" and expect[1] != value):
                        raise Exception("unexpected " + value)

            # if none of that goes than add this element to the chain
            temp_chain.append((pattern, value))
            # remove the element from the
            data.pop(0)

            # matching the result
            match_result = self.match(temp_chain)

            # list of expected elements next
            expect_next = match_result[0]
            # this var stocks the action to take
            action = match_result[1]
            # in case of recursive cal required this is the name of the rule its supposed to find
            exp_rule = match_result[2]
            # in case a full match found with a rule this hold the name of the rule
            rule = match_result[3]

            # processing the outcome of the match
            # 0 means no match rule found
            if action == 0:
                raise Exception("syntax error! at " + value)

            # 1 means at least one rule was found
            elif action == 1:
                pass

            # 2 means a rule was found and it was complete
            elif action == 2:
                # if no rule is expected ( not in recursive call)
                if expect_rule == None:
                    self.result.append((temp_chain, rule))
                else:
                    # if the result matches the expected rule
                    if self.check(expect_next, temp_chain):
                        # save the data and return the result
                        self.data = data
                        return temp_chain
                    else:
                        raise Exception("Syntax error!")
            # 3 means a recursive call with a certain rule to expect
            elif action == 3:
                self.result.append((self.parse(data, exp_rule), exp_rule))
                data = self.data

        return self.result
