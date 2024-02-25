def play_game
  puts "Welcome to the game of Rock, Paper, Scissors!"
  puts "Enter option(play/end):"
  start = gets.chomp()

  if start == "end"
    puts "Adios"
    return
  end

  guess = false
  game = 0

  while game != 3
    array = ["rock","paper","scissors"]
    computer = array.sample()
    puts "Enter option(rock/paper/scissors): "
    player = gets.chomp()
    game +=1

    if computer == player
      puts "It's a tie"
    elsif (computer == "rock" and player == "scissors") 
         (computer == "paper" and player == "rock") 
         (computer == "scissors" and player == "paper")
      puts "Computer won"
    else
      puts "You won!!"
    end

    puts "Good game"
    guess = true
  end
end

play_game
