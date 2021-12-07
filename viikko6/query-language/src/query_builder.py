from matchers import *
from stack import Stack

class QueryBuilder:
    def __init__(self, stack = Stack()):
        self.stack = stack

    def playsIn(self, team):
        self.stack.push(PlaysIn(team))
        return QueryBuilder(self.stack)

    def hasAtLeast(self, value, attr):
        self.stack.push(HasAtLeast(value, attr))
        return QueryBuilder(self.stack)

    def notMatch(self, matcher):
        self.stack.push(Not(matcher))
        return QueryBuilder(self.stack)

    def hasFewerThan(self, value, attr):
        self.stack.push(HasFewerThan(value, attr))
        return QueryBuilder(self.stack)

    def all(self):
        self.stack.pusk(All())
        return QueryBuilder(self.stack)

    def orMatch(self, *matchers):
        self.stack.push(Or(matchers))
        return QueryBuilder(self.stack)

    def build(self):
        matchers = self.stack.stack
        return And(matchers)
