""" Puzzle 1 and 2 """
#!/usr/bin/python3
from day9_lib import Day9lib
from day9_lib import InputLoc

class NextValuePredictor(Day9lib):
    """ Puzzle 1 and 2 solution """
    sum_of_prediction = 0

    def __init__(self):
        pass

    def run(self):
        """ Run method """
        self.main()

    def main(self):
        """ Main method """
        # Use either SAMPLE_INPUT_1 or ORIGINAL_INPUT
        content = self.read_file_content(InputLoc.ORIGINAL_INPUT)

        sum_of_next_prediction = 0
        sum_of_prev_history = 0

        for line in content:
            x = list( map(int, line.split() ) )
            sum_of_next_prediction += self.next_value_predict(x)
        print(f"Answer is puzzle 1 : {sum_of_next_prediction}")

        for line in content:
            x = list( map(int, line.split() ) )
            sum_of_prev_history += self.next_value_predict(x, history=True)
        print(f"Answer is puzzle 2 : {sum_of_prev_history}")

        return (sum_of_next_prediction, sum_of_prev_history)

if __name__ == "__main__":
    nextValuePredictor = NextValuePredictor()
    nextValuePredictor.run()
