game = 0
puts "Welcome to the game of Rock, Paper, Scissors!"
puts "Enter option(play/end):"
start = gets.chomp()
guess = false
while start != "end" and !guess
    if game != 3
        array = ["rock","paper","scissors"]
        computer = array.sample()
        puts "Enter option(rock/paper/scissors): "
        player = gets.chomp()
        game +=1
    else
        guess = true
    end
    if computer == player
        puts "Its a tie"
    elsif computer == "rock" and player == "scissors"
        puts "Computer won"
    elsif computer == "paper" and player == "rock"
        puts "Computer won"
    elsif computer == "scissors" and player == "paper"
        puts "Computer won"

    else
        puts "You won!!"
  break
    end
end
if guess == true or start == "end"
    puts "Adios"
else
    puts "Good game"
end
