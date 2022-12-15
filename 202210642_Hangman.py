HANGMAN = [
    '________',
    '|       |',
    '|       O',
    '|       |',
    '|      /|\ ',
    '|       |',
    '|      / \ '
]

WORDS = [
    'casa', 'car', 'mono', 'elevator', 'python', 'java',
    'pleasure', 'young', 'festival', 'sing', 'class'
]

class Hangman():
    """
    The hangman game class 
    """

    def __init__(self, word_to_guess):
        self.failed_attempts = 0
        self.word_to_guess = word_to_guess
        self.game_progress = list('_'*len(word_to_guess)) # 

    def find_indexes(self, letter):
        """
        입력된 글자 하나를 맞추고자 하는 단어 안에서의 인덱스와 함께 반환. 
        letter 는 string, 인덱스를 찾고자하는 하나의 글자. 
        """
        return [i for i, char in enumerate(self.word_to_guess) if letter == self.word_to_guess[i]]

    def is_invalid_letter(self, input_):
        """
        플레이어가 입력한 글자가 1개 이상의 글자이거나 숫자인지 판별.
        isalpha() 의 기능을 찾아 이해하고, 사용할 것. 
        i) 글자일 경우, 글자이면서 동시에 입력받은 글자의 길이가 1이상이면 True 
        ii) 숫자인 경우에도 True 반환 
        --> 이 값들이 참일 경우, 다시 입력하라는 메시지가 play() 에서 진행. 
        input_ 은 string 으로 유요한지 판별해야하는 인풋값. 
        """
        return (input_.isdigit()) or (input_.isalpha() and len(input_)>1)

    def print_game_status(self):
        """
        실패할 때마다 행맨 그림을 한줄씩 추가해서 그려주는 부분 
        문자열의 join() 메소드를 적용하여 HANGMAN 리스트의 아스키그림이 
        한줄마다 출력되도록 함. 
        행맨 그림이 다 그려진 후, 남아있는 글자의 언더바 (_) 와 밝혀진 글자들이 출력되도록 함. 
        """
        print('\n')
        print('\n'.join(HANGMAN[:self.failed_attempts]))
        print('\n')
        print(' '.join(self.game_progress))


    def update_progress(self, letter, indexes):
        """
        사용자가 추측한 글자가 맞춰야하는 단어에 있으면, 해당 글자의 인덱스를 함께 받아서, self.game_progress 를 업데이트 함. 
        letter 는 string, game progress 에 추가되어야하는 글자. 
        indexes 는 list 형태로,해당 글자의 단어에서의 인덱스. 
        """
        for index in indexes:
            self.game_progress[index] = letter

    def get_user_input(self):
        """ 
        플레이어로부터 추측하는 글자를 입력받아 user_input 에 할당. 
        """
        user_input = input('\nPlease type a letter: ')
        return user_input

    def play(self):
        """
        게임을 진행하는 부분. 
        플레이어가 행맨 그림이 다 완성되기 전에 글자를 맞추면 성공 
        그렇지 못하면 실패하여 종료됨. 
        """
        while True:
            print(self.game_progress) # 현재 게임 상태를 먼저 출력해줌.
            self.print_game_status() 
            user_input = self.get_user_input() # user_input 을 입력받는 메소드 적용. 

            # Validate the user input
            if self.is_invalid_letter(user_input) == True : # 플레이어가 입력한 인풋이 유효한 값인지 아닌지. 
                print('제대로 입력하세요')# 아니면, 제대로 입력하라는 메세지 출력하고
                continue# break or continue 중 하나를 사용하여 계속 입력 받음. 
            
            # Check if the letter is not already guessed
            if user_input in self.game_progress :
                print('이미 입력받은 알파벳 입니다')# 이미 입력받았던 알파벳이면, 이미 입력했다 메시지 출력
                continue# break or continue 중 하나를 사용하여 계속 입력

            # when the user_input is a character in word_to_guess
            if user_input in self.word_to_guess :
                indexes = self.find_indexes(user_input) # 추측한 글자의 인덱스 받기 
                self.update_progress(user_input, indexes) # 입력받은 글자로 현재 게임 상태 업데이트 

                # If there is no letter to find in the word
                if not '_' in self.game_progress : # 더이상 맞출 글자가 없으면 
                    print('\n------Yay! You win!')
                    print('The word is: {0}'.format(self.word_to_guess))
                    break
            else:
                self.failed_attempts += 1

            if self.failed_attempts >= len(HANGMAN) : 
              print("\n-----You lost!")
              break

import random
if __name__ == '__main__':
    word_to_guess = random.choice(WORDS)
    hangman = Hangman(word_to_guess)
    hangman.play()