# Alexandar Lackovic and Fied Elahresh
# FSE GAME.py
# This program is a game closely inspired by "Jetpack Joyride" and is called "Ralph's Rampage". The game is a side scroller featuring three levels increasing in difficulty, they are held in the main page called campaign. Within the levels, you need to dodge obstacles like lasers and bombs, while also collecting coins and trying to reach the end so you can progress to the next level.
# The program also features a shop page where you can purchase cosmetics with the coins you earn in game, the skins you buy are saved using File input and output. It also has a settings page where you can prestige, mute music and sound effects, and even show FPS.
# And finally a arcade page, where you can play Ralph's Rampage but it is infinite and speeds up as you progress. The arcade also holds high scores for this game mode with distance travelled, and coins collected. if you are really skilled and you reach the end, there is a surprise waiting for you.
from pygame import *
from random import *

screen = display.set_mode((1920, 1080))
display.set_caption("Ralph's Rampage")
myClock = time.Clock()

# Initializing music and fonts
font.init()
mixer.init()

nebulaFont = font.Font("data/Nebula-Regular.otf", 50)
mixer.music.load("data/menuMusic.mp3")

# Loading in graphics
menuBackground = image.load("data/menuBackground.jpg").convert()
gameLogo = image.load("data/gameLogo.png")
showcaseSkin1 = image.load("data/showcaseSkin1.png")
showcaseSkin2 = image.load("data/showcaseSkin2.png")
showcaseSkin3 = image.load("data/showcaseSkin3.png")
background1 = image.load("data/background.png").convert()
background2 = image.load("data/background.png").convert()
campaignButton = image.load("data/campaignNormal.png")
campaignButtonHover = image.load("data/campaignHover.png")
campaignButtonPressed = image.load("data/campaignPressed.png")
backButton = image.load("data/backNormal.png")
backButtonHover = image.load("data/backHover.png")
backButtonPressed = image.load("data/backPressed.png")
arcadeButton = image.load("data/arcadeNormal.png")
arcadeButtonHover = image.load("data/arcadeHover.png")
arcadeButtonPressed = image.load("data/arcadePressed.png")
settingsButton = image.load("data/settingsNormal.png")
settingsButtonHover = image.load("data/settingsHover.png")
settingsButtonPressed = image.load("data/settingsPressed.png")
shopButton = image.load("data/shopNormal.png")
shopButtonHover = image.load("data/shopHover.png")
shopButtonPressed = image.load("data/shopPressed.png")
lvl1ButtonNormal = image.load("data/level1Normal.png")
lvl1ButtonHover = image.load("data/level1Hover.png")
lvl2ButtonLocked = image.load("data/level2Locked.png")
lvl2ButtonNormal = image.load("data/level2Normal.png")
lvl2ButtonHover = image.load("data/level2Hover.png")
lvl3ButtonLocked = image.load("data/level3Locked.png")
lvl3ButtonNormal = image.load("data/level3Normal.png")
lvl3ButtonHover = image.load("data/level3Hover.png")
laserOn = image.load("data/laserOn.png")
laserOff = image.load("data/laserOff.png")
plateNormal = image.load("data/plateNormal.png")
continueButtonNormal = image.load("data/continueButtonNormal.png")
continueButtonHover = image.load("data/continueButtonHover.png")
returnToMenuButtonNormal = image.load("data/returnButtonNormal.png")
returnToMenuButtonHover = image.load("data/returnButtonHover.png")
gameOverLevels = image.load("data/levelsGameOver.png")
gameOverArcade = image.load("data/gameOverArcade.png")
skin1ImageNormal = image.load("data/shopSkin1Normal.png")
skin1ImageHover = image.load("data/shopSkin1Hover.png")
skin2ImageNormal = image.load("data/shopSkin2Normal.png")
skin2ImageHover = image.load("data/shopSkin2Hover.png")
skin2ImageLocked = image.load("data/shopSkin2Locked.png")
skin3ImageNormal = image.load("data/shopSkin3Normal.png")
skin3ImageHover = image.load("data/shopSkin3Hover.png")
skin3ImageLocked = image.load("data/shopSkin3Locked.png")
shopTitle = image.load("data/shopTitleImage.png")
settingsTitle = image.load("data/settingsTitleImage.png")
levelsTitle = image.load("data/levelsTitleImage.png")
arcadeTitle = image.load("data/arcadeTitle.png")
prestigeButtonNormal = image.load("data/prestigeButtonNormal.png")
prestigeButtonHover = image.load("data/prestigeButtonHover.png")
prestigeButtonPressed = image.load("data/prestigeButtonPressed.png")
insufficientFundsImage = image.load("data/insufficientFundsImage.png")
bombImage = image.load("data/bombImage.png")
skin1Selected = image.load("data/shopSkin1Selected.png")
skin2Selected = image.load("data/shopSkin2Selected.png")
skin3Selected = image.load("data/shopSkin3Selected.png")
skin2LockedHover = image.load("data/shopSkin2LockedHover.png")
skin3LockedHover = image.load("data/shopSkin3LockedHover.png")
prestigeMaster = image.load("data/prestigeMaster.png")
congratsScreen = image.load("data/congratsScreen.png")
nextLevelButtonNormal = image.load("data/nextLevelButtonNormal.png")
nextLevelButtonHover = image.load("data/nextLevelButtonHover.png")
arcadeInformationImage = image.load("data/arcadeInformationPage.png")
playArcadeButtonNormal = image.load("data/playArcadeButtonNormal.png")
playArcadeButtonHover = image.load("data/playArcadeButtonHover.png")
playAgainButtonNormal = image.load("data/playAgainButtonNormal.png")
playAgainButtonHover = image.load("data/playAgainButtonHover.png")
arcadeWinPage = image.load("data/arcadeWin.png")
settingsPageImage = image.load("data/settingsPageImage.png")
unmuteNormal = image.load("data/unmuteNormal.png")
unmuteHover = image.load("data/unmuteHover.png")
unmuteSelected = image.load("data/unmuteSelected.png")
muteNormal = image.load("data/muteNormal.png")
muteHover = image.load("data/muteHover.png")
muteSelected = image.load("data/muteSelected.png")
checkNormal = image.load("data/checkNormal.png")
checkHover = image.load("data/checkHover.png")
checkSelected = image.load("data/checkSelected.png")
uncheckNormal = image.load("data/uncheckNormal.png")
uncheckHover = image.load("data/uncheckHover.png")
uncheckSelected = image.load("data/uncheckSelected.png")

# Rectangles to allow for interaction with buttons
campaignRect = Rect(85, 855, campaignButton.get_width(), campaignButton.get_height())
arcadeRect = Rect(450, 855, arcadeButton.get_width(), arcadeButton.get_height())
shopRect = Rect(1144, 855, shopButton.get_width(), shopButton.get_height())
settingsRect = Rect(1509, 855, settingsButton.get_width(), settingsButton.get_height())
backRect = Rect(50, 50, backButton.get_width(), backButton.get_height())
continueRect = Rect(618, 635, continueButtonNormal.get_width(), continueButtonNormal.get_height())
playAgainRect = Rect(618, 635, playAgainButtonNormal.get_width(), playAgainButtonNormal.get_height())
nextLevelRect = Rect(618, 635, returnToMenuButtonNormal.get_width(), returnToMenuButtonNormal.get_height())
returnToMenuRect = Rect(976, 635, returnToMenuButtonNormal.get_width(), returnToMenuButtonNormal.get_height())
level1Rect = Rect(396, 320, lvl1ButtonNormal.get_width(), lvl1ButtonNormal.get_height())
level2Rect = Rect(797, 320, lvl2ButtonNormal.get_width(), lvl2ButtonNormal.get_height())
level3Rect = Rect(1198, 320, lvl3ButtonNormal.get_width(), lvl3ButtonNormal.get_height())
skin1Rect = Rect(396, 320, skin1ImageNormal.get_width(), skin1ImageNormal.get_height())
skin2Rect = Rect(797, 320, skin2ImageNormal.get_width(), skin2ImageNormal.get_height())
skin3Rect = Rect(1198, 320, skin3ImageNormal.get_width(), skin3ImageNormal.get_height())
fpsCheckRect = Rect(964, 335, checkNormal.get_width(), checkNormal.get_height())
fpsUncheckRect = Rect(1064, 335, checkNormal.get_width(), checkNormal.get_height())
soundEffectsUnmuteRect = Rect(1172, 420, checkNormal.get_width(), checkNormal.get_height())
soundEffectsMuteRect = Rect(1272, 420, checkNormal.get_width(), checkNormal.get_height())
musicUnmuteRect = Rect(816, 505, checkNormal.get_width(), checkNormal.get_height())
musicMuteRect = Rect(916, 505, checkNormal.get_width(), checkNormal.get_height())
settingsPageImageRect = settingsPageImage.get_rect(midtop=(screen.get_width()/2, 275))
titleRect = shopTitle.get_rect(midtop=(screen.get_width()/2, 75))
prestigeRect = prestigeButtonNormal.get_rect(midbottom=(screen.get_width()/2, screen.get_height() - 165))
gameEndRect = gameOverLevels.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
arcadeInformationRect = arcadeInformationImage.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
logoRect = gameLogo.get_rect(midtop=(screen.get_width()/2, 50))
showcaseRect = showcaseSkin1.get_rect(midbottom=(screen.get_width() / 2, 1080))
insufficientFundsRect = insufficientFundsImage.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
playArcadeButtonRect = playArcadeButtonNormal.get_rect(midtop=(screen.get_width()/2, 650))
returnToMenuRectMiddle = returnToMenuButtonNormal.get_rect(midtop=(screen.get_width()/2, 635))
arcadeReturnRectMiddle = returnToMenuButtonNormal.get_rect(midtop=(screen.get_width()/2, 660))

running = True
speed = 8
frame = 0
level = 1
playerY = 800
gameMode = "menu"
backgroundX1 = 0
backgroundX2 = background1.get_width()
scrollCount = 0
verticalVelocity = 0
gravity = 1
jumpSpeed = -12
scrollSpeed = 1
arcadeScrollSpeed = 1
deadAnimTimer = 0
immuneTimer = 0
winTimer = 0
laserPositions = []
arcadeLaserPositions = []
staticCoinPositions = []
arcadeStaticCoinPositions = []
dynamicCoinPositions = []
arcadeDynamicCoinPositions = []
bombPositions = []
arcadeBombPositions = []
playerDead = False
arcadePlayerDead = False
deadMan = False
playerWon = False
arcadePlayerWon = False
totalDistancePixels = 0
insufficientFundsError = 0
amountInsufficient = 0
arcadeScore = 0
immune = False
coinsAdded = False
flyAnimations = []
runAnimations = []
jumpAnimations = []
landAnimations = []
deathAnimations = []
winAnimations = []
confettiPosX = []    # List that will store the confetti X positions
confettiPosY = []    # List that will store the confetti Y positions
confettiTransparency = []    # List that will store all of the transparency/alpha values for the confetti
confettiSize = []    # List that will store the size of the confetti
confettiSpeed = []    # List that will store the confetti speeds
confettiGenerated = False    # Whether or not the confetti has been generated
bombDeath = False

coinsCollected = 999

level2Locked = True
level3Locked = True
skin2Locked = True
skin3Locked = True
coinsInAccount = 500
selectedCharacter = 0    # 0 - First Colour 1 - Second Colour 2 - Third Colour
coinMultiplier = 1
prestigeAlready = 0
arcadeHighscore = 0
arcadeCoinsHighscore = 0
showFPS = True
soundEffectsMuted = False
musicMuted = False

if not musicMuted:
    mixer.music.play(-1)
elif musicMuted:
    mixer.music.pause()
laserDeath = mixer.Sound("data/laserDeath.mp3")
coinCollect = mixer.Sound("data/coinEaten.mp3")
explosionSound = mixer.Sound("data/bombExploding.mp3")


def readData():
    # Function that reads all of the data from the "gameInformation" txt file. This data is then assigned to variables that are used throughout the game.
    global level2Locked, level3Locked, skin2Locked, skin3Locked, coinsInAccount, selectedCharacter, coinMultiplier, prestigeAlready, arcadeHighscore, arcadeCoinsHighscore, showFPS, soundEffectsMuted, musicMuted
    infoFile = open("data/gameInformation.txt")    # Opening the information file
    level2LockedFile = int(infoFile.readline())
    level3LockedFile = int(infoFile.readline())
    skin2LockedFile = int(infoFile.readline())
    skin3LockedFile = int(infoFile.readline())
    coinsInAccount = int(infoFile.readline())
    selectedCharacter = int(infoFile.readline())  # 0 - First Colour 1 - Second Colour 2 - Third Colour
    coinMultiplier = int(infoFile.readline())    # 1 - Normal 5 - Prestige Master Multiplier
    prestigeAlreadyFile = int(infoFile.readline())    # 0 - Not Happened Already 1 - Happened Already
    arcadeHighscore = int(infoFile.readline())
    arcadeCoinsHighscore = int(infoFile.readline())
    showFPSFile = int(infoFile.readline())    # 0 - Don't Show 1 - Show
    soundEffectsMutedFile = int(infoFile.readline())    # 0 - Not Muted 1 - Muted
    musicMutedFile = int(infoFile.readline())

    infoFile.close()

    if level2LockedFile == 0:    # Assigning the correct Boolean values to the variables that will be used throughout
        level2Locked = False
    elif level2LockedFile == 1:
        level2Locked = True

    if level3LockedFile == 0:
        level3Locked = False
    elif level3LockedFile == 1:
        level3Locked = True

    if skin2LockedFile == 0:
        skin2Locked = False
    elif skin2LockedFile == 1:
        skin2Locked = True

    if skin3LockedFile == 0:
        skin3Locked = False
    elif skin3LockedFile == 1:
        skin3Locked = True

    if prestigeAlreadyFile == 0:
        prestigeAlready = False
    elif prestigeAlreadyFile == 1:
        prestigeAlready = True

    if showFPSFile == 0:
        showFPS = False
    elif showFPSFile == 1:
        showFPS = True

    if soundEffectsMutedFile == 0:
        soundEffectsMuted = False
    elif soundEffectsMutedFile == 1:
        soundEffectsMuted = True

    if musicMutedFile == 0:
        musicMuted = False
    elif musicMutedFile == 1:
        musicMuted = True


def writeData():
    #    Function that writes the data to the "gameInformation" txt file. This data includes variables used in the game that may have changed.
    outputFile = open("data/gameInformation.txt", "w")    # Opening the file to overwrite any existing content
    
    if level2Locked:    # Assigning the correct numerical values based off of the Boolean values used throughout the game
        level2LockedFile = 1
    elif not level2Locked:
        level2LockedFile = 0

    if level3Locked:
        level3LockedFile = 1
    elif not level3Locked:
        level3LockedFile = 0

    if skin2Locked:
        skin2LockedFile = 1
    elif not skin2Locked:
        skin2LockedFile = 0

    if skin3Locked:
        skin3LockedFile = 1
    elif not skin3Locked:
        skin3LockedFile = 0

    if prestigeAlready:
        prestigeAlreadyFile = 1
    elif not prestigeAlready:
        prestigeAlreadyFile = 0

    if showFPS:
        showFPSFile = 1
    elif not showFPS:
        showFPSFile = 0

    if soundEffectsMuted:
        soundEffectsMutedFile = 1
    elif not soundEffectsMuted:
        soundEffectsMutedFile = 0

    if musicMuted:
        musicMutedFile = 1
    elif not musicMuted:
        musicMutedFile = 0
    
    # Actually writing all of the data then closing the file
    outputFile.write("{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(level2LockedFile, level3LockedFile, skin2LockedFile, skin3LockedFile, coinsInAccount, selectedCharacter, coinMultiplier, prestigeAlreadyFile, arcadeHighscore, arcadeCoinsHighscore, showFPSFile, soundEffectsMutedFile, musicMutedFile))
    outputFile.close()


readData()    # Calling on the function to read the data


class Animation:    # Class for animations that makes displaying much easier
    def __init__(self, imagePrefix, count):
        self.imageCount = count    # imageCount is now the same as count
        self.images = []    # images is a blank list

        for i in range(self.imageCount):    # Looping through the length of images (image count/number if images)
            filename = "data/" + imagePrefix + "{:0>5}".format(i) + ".png"    # Using {:0>5} to number format 'i' into a 5 length 5 field fill with 0s
            self.images.append(image.load(filename))    # Loading and adding the images to the images list

    def display(self, xposition, yposition):
        imageIndex = frame // speed % self.imageCount    # Finding image the animation is on
        screen.blit(self.images[imageIndex], (xposition, yposition))    # Displaying the image at the x and y position


runCol1Animation = Animation("RunCol1", 6)    # Initializing the animations
flyCol1Animation = Animation("FlyCol1", 6)
wonCol1Animation = Animation("WonCol1", 13)
jumpCol1Animation = Animation("JumpCol1", 5)
landCol1Animation = Animation("LandCol1", 4)
deathCol1Animation = Animation("DeathCol1", 6)
runCol2Animation = Animation("RunCol2", 6)
flyCol2Animation = Animation("FlyCol2", 6)
wonCol2Animation = Animation("WonCol2", 13)
jumpCol2Animation = Animation("JumpCol2", 5)
landCol2Animation = Animation("LandCol2", 4)
deathCol2Animation = Animation("DeathCol2", 6)
runCol3Animation = Animation("RunCol3", 6)
flyCol3Animation = Animation("FlyCol3", 6)
wonCol3Animation = Animation("WonCol3", 13)
jumpCol3Animation = Animation("JumpCol3", 5)
landCol3Animation = Animation("LandCol3", 4)
deathCol3Animation = Animation("DeathCol3", 6)
coinAnimation = Animation("coinStatic", 6)
explosionAnimation = Animation("explosion", 15)

runAnimations.append(runCol1Animation)    # Appending the animations to the lists for their corresponding action (All colours of each action are in the lists)
runAnimations.append(runCol2Animation)
runAnimations.append(runCol3Animation)
flyAnimations.append(flyCol1Animation)
flyAnimations.append(flyCol2Animation)
flyAnimations.append(flyCol3Animation)
winAnimations.append(wonCol1Animation)
winAnimations.append(wonCol2Animation)
winAnimations.append(wonCol3Animation)
jumpAnimations.append(jumpCol1Animation)
jumpAnimations.append(jumpCol2Animation)
jumpAnimations.append(jumpCol3Animation)
landAnimations.append(landCol1Animation)
landAnimations.append(landCol2Animation)
landAnimations.append(landCol3Animation)
deathAnimations.append(deathCol1Animation)
deathAnimations.append(deathCol2Animation)
deathAnimations.append(deathCol3Animation)


def menuInteraction():
    # Function that is responsible for the interactions on the menu page. Displays hover images where needed and changes pages if clicked correctly
    global gameMode
    if campaignRect.collidepoint(mx, my):    # Sending to new page if certain buttons are clicked
        if click:
            gameMode = "levelsPage"
        elif mb[0]:
            screen.blit(campaignButtonPressed, campaignRect)
        else:
            screen.blit(campaignButtonHover, campaignRect)
    if arcadeRect.collidepoint(mx, my):
        if click:
            gameMode = "arcadeMode"
        elif mb[0]:
            screen.blit(arcadeButtonPressed, arcadeRect)
        else:
            screen.blit(arcadeButtonHover, arcadeRect)
    if shopRect.collidepoint(mx, my):
        if click:
            gameMode = "shop"
        elif mb[0]:
            screen.blit(shopButtonPressed, shopRect)
        else:
            screen.blit(shopButtonHover, shopRect)
    if settingsRect.collidepoint(mx, my):
        if click:
            gameMode = "settingsPage"
        elif mb[0]:
            screen.blit(settingsButtonPressed, settingsRect)
        else:
            screen.blit(settingsButtonHover, settingsRect)


def levelsPageInteraction():
    # Function that is responsible for the interactions on the levels page. Displays hover images where needed, changes pages if clicked correctly, starts the game
    global gameMode, level
    if level1Rect.collidepoint(mx, my):    # Sending you to the three levels dependant on what level you click (1,2,3)
        if click:
            gameMode = "playGame"
            level = 1
            setupLevel()    # Calls the function that makes sure that all of the important values are correctly reset
        else:
            screen.blit(lvl1ButtonHover, level1Rect)
    if level2Rect.collidepoint(mx, my):
        if not level2Locked:    # To go to level 2 you need to have it unlocked
            if click:
                gameMode = "playGame"
                level = 2
                setupLevel()
            else:
                screen.blit(lvl2ButtonHover, level2Rect)
    if level3Rect.collidepoint(mx, my):
        if not level3Locked:    # To go to level 3 you need to have it unlocked
            if click:
                gameMode = "playGame"
                level = 3
                setupLevel()
            else:
                screen.blit(lvl3ButtonHover, level3Rect)


def gameOverInteraction():
    # Function that is responsible for the interactions on the game over page. Displays hover images where needed and changes pages if clicked correctly
    global gameMode, coinsAdded, coinsInAccount, playerDead, deadMan, immune, insufficientFundsError, amountInsufficient
    if not coinsAdded:    # After you die it adds the collected coins to your total coins
        coinsInAccount += coinsCollected * coinMultiplier
        coinsAdded = True
    if continueRect.collidepoint(mx, my):    # If you spend 5 coins to continue, all of the necessary values are reset
        if click and coinsInAccount >= 5:
            playerDead = False
            deadMan = False
            immune = True
            gameMode = "playGame"
            coinsInAccount -= 5
            coinsAdded = False
        elif click and coinsInAccount < 5:    # If you don't have enough coins, the error time will become 3 seconds (this will set the error off)
            insufficientFundsError = 165
            amountInsufficient = 5 - coinsInAccount    # However much you are short is calculated so that it can also be displayed
        else:
            screen.blit(continueButtonHover, continueRect)
    if returnToMenuRect.collidepoint(mx, my):    # Return to menu
        if click:
            gameMode = "menu"
        else:
            screen.blit(returnToMenuButtonHover, returnToMenuRect)


def winPageInteraction():
    # Function that is responsible for the interactions on the win page. Displays hover images where needed and changes pages if clicked correctly
    global gameMode, level
    if level != 3:    # If you aren't on level 3 you could continue or return to menu
        if nextLevelRect.collidepoint(mx, my):    # Starts the next level for you
            if click:
                gameMode = "playGame"
                level = level + 1
                setupLevel()
            else:
                screen.blit(nextLevelButtonHover, nextLevelRect)
        if returnToMenuRect.collidepoint(mx, my):
            if click:
                gameMode = "menu"
            else:
                screen.blit(returnToMenuButtonHover, returnToMenuRect)
    else:    # If you are on level 3 you could only go back to menu
        if returnToMenuRectMiddle.collidepoint(mx, my):
            if click:
                gameMode = "menu"
            else:
                screen.blit(returnToMenuButtonHover, returnToMenuRectMiddle)


def shopInteraction():
    # Function that is responsible for the interactions on the shop page. Displays hover images where needed and changes pages if clicked correctly
    global selectedCharacter, skin2Locked, skin3Locked, coinsInAccount, insufficientFundsError, amountInsufficient
    if skin1Rect.collidepoint(mx, my):
        if click:
            selectedCharacter = 0
        elif selectedCharacter != 0:
            screen.blit(skin1ImageHover, skin1Rect)
    if skin2Rect.collidepoint(mx, my):
        if skin2Locked:
            if click and coinsInAccount >= 50:    # To buy this skin you need 50 coins
                coinsInAccount -= 50
                skin2Locked = False
                selectedCharacter = 1
            elif click and coinsInAccount < 50:    # If you don't have enough coins, you can't buy the skin and the error will appear
                insufficientFundsError = 165
                amountInsufficient = 50 - coinsInAccount
            else:
                screen.blit(skin2LockedHover, skin2Rect)
        else:
            if click:
                selectedCharacter = 1
            elif selectedCharacter != 1:
                screen.blit(skin2ImageHover, skin2Rect)
    if skin3Rect.collidepoint(mx, my):
        if skin3Locked:
            if click and coinsInAccount >= 250:    # This skin is 250 coins
                coinsInAccount -= 250
                skin3Locked = False
                selectedCharacter = 2
            elif click and coinsInAccount < 250:
                insufficientFundsError = 165
                amountInsufficient = 250 - coinsInAccount
            else:
                screen.blit(skin3LockedHover, skin3Rect)
        else:
            if click:
                selectedCharacter = 2
            elif selectedCharacter != 2:
                screen.blit(skin3ImageHover, skin3Rect)


def confetti():
    # Function that is responsible for the generation, movement, and display of all confetti
    global confettiGenerated, confettiSpeed, confettiPosX, confettiPosY, confettiSize, confettiTransparency
    if not confettiGenerated:  # If the confetti has not been generated, generate 750 confetti with:
        for i in range(750):
            confettiPosX.append(randint(0, screen.get_width()))  # Random x positions
            confettiPosY.append(-1 * randint(0, screen.get_height()))  # Random y positions off of the screen
            confettiTransparency.append(randint(50, 255))  # Random colors
            confettiSize.append(randint(1, 4))  # Random sizes between 1 and 4
            confettiSpeed.append(randint(1, 5))  # And random speeds at which they will fall
        confettiGenerated = True  # Saying that the confetti has been generated
    for i in range(750):  # Drawing all of the confetti at their respective x and y positions, in their respective color and size
        draw.circle(screen, (255, 255, 255, confettiTransparency[i]), (confettiPosX[i], confettiPosY[i]), confettiSize[i])
        confettiPosY[i] += confettiSpeed[i]  # Making the confetti fall by adding their respective speeds to the y value
        if confettiPosY[i] >= screen.get_height():  # If the confetti's y position is >= to the screen, the y position is reset to 0
            confettiPosY[i] = 0


def setupLevel():
    # Function that is responsible for the placing obstacles on the page, resetting important values and setting up the speed and background
    global scrollSpeed, coinsCollected, playerDead, coinsAdded, totalDistancePixels, backgroundX1, backgroundX2, bombDeath, deadMan, playerWon
    if not musicMuted:
        mixer.music.pause()
    scrollSpeed = 8 + level * 3
    createLasers()
    createCoins()
    createBombs()
    coinsCollected = 0
    totalDistancePixels = 0
    backgroundX1 = 0
    backgroundX2 = background1.get_width()
    playerDead = False
    deadMan = False
    coinsAdded = False
    bombDeath = False
    playerWon = False


def displayBackButton():
    # Function that is responsible for the interaction with the back button. It brings you back to the menu.
    global gameMode, click, mb, mx, my
    screen.blit(backButton, backRect)
    if backRect.collidepoint(mx, my) and insufficientFundsError == 0:    # You could only use it if there isn't an error
        if click:
            gameMode = "menu"
        elif mb[0]:
            screen.blit(backButtonPressed, backRect)
        else:
            screen.blit(backButtonHover, backRect)


def drawMenu():
    # Function that is responsible for "drawing" all of the things on the menu page.
    screen.blit(menuBackground, (0, 0))
    confetti()
    screen.blit(gameLogo, logoRect)
    screen.blit(campaignButton, campaignRect)
    screen.blit(arcadeButton, arcadeRect)
    screen.blit(shopButton, shopRect)
    screen.blit(settingsButton, settingsRect)
    if selectedCharacter == 0:
        screen.blit(showcaseSkin1, showcaseRect)
    if selectedCharacter == 1:
        screen.blit(showcaseSkin2, showcaseRect)
    if selectedCharacter == 2:
        screen.blit(showcaseSkin3, showcaseRect)


def drawLevelsPage():
    # Function that is responsible for "drawing" all of the things on the levels page.
    screen.blit(menuBackground, (0, 0))
    confetti()
    screen.blit(levelsTitle, titleRect)
    displayBackButton()
    screen.blit(lvl1ButtonNormal, level1Rect)
    if level2Locked:
        screen.blit(lvl2ButtonLocked, level2Rect)
    else:
        screen.blit(lvl2ButtonNormal, level2Rect)
    if level3Locked:
        screen.blit(lvl3ButtonLocked, level3Rect)
    else:
        screen.blit(lvl3ButtonNormal, level3Rect)


def moveScene():
    # Function that is responsible for "drawing" the scene and moving it.
    global backgroundX1, backgroundX2, level, scrollSpeed, totalDistancePixels
    screen.blit(background1, (backgroundX1, 0))
    screen.blit(background2, (backgroundX2, 0))
    if not playerDead:
        if totalDistancePixels > -29760:    # If we haven't reached the end of the level (4 times through the background - half of the screen size)
            backgroundX1 -= scrollSpeed
            backgroundX2 -= scrollSpeed
            totalDistancePixels -= scrollSpeed
    if backgroundX1 <= -background1.get_width():    # Resetting the backgrounds if they go fully negative
        backgroundX1 = backgroundX2 + background1.get_width()
    if backgroundX2 <= -background2.get_width():
        backgroundX2 = backgroundX1 + background2.get_width()


def movePlayer():
    # Function that is responsible for movement and display of the character.
    global verticalVelocity, playerY, gameMode, deadMan
    # Moving the player
    if totalDistancePixels <= -29450:
        if playerY > 800:    # Making sure the character does not fall below the ground
            playerY = 800
            verticalVelocity = 0
        verticalVelocity += gravity
    else:
        if not playerDead and not playerWon:
            if playerY > 800:    # Making sure they don't go too low
                playerY = 800
                verticalVelocity = 0
            elif playerY < 25:    # Making sure they don't go too high
                playerY = 25
            if playerY < 800:
                verticalVelocity += gravity    # Adding gravity if they are above the ground
            if flying and totalDistancePixels > -29660:    # Giving the character the upwards motion needed to fly
                verticalVelocity = jumpSpeed
        elif playerDead:
            verticalVelocity += gravity
            if playerY > 800:
                playerY = 800
                verticalVelocity = 0
    playerY += verticalVelocity    # Constantly adding VV to the player (gravity and jump speed, if any)

    # Displaying the animations
    if not playerDead:
        if flying:
            if playerY > 700:  # Jump zone means he jumps here
                jumpAnimations[selectedCharacter].display(640, playerY)
            else:    # Fly Zone means he flies here
                flyAnimations[selectedCharacter].display(640, playerY)
        else:
            if totalDistancePixels > -29760 and playerY == 800:    # Run if on the ground
                runAnimations[selectedCharacter].display(640, playerY)
            elif playerWon:
                winAnimations[selectedCharacter].display(640, playerY)    # Celebrate if won
            else:
                landAnimations[selectedCharacter].display(640, playerY)    # Land if falling
    else:
        if playerY < 800:
            landAnimations[selectedCharacter].display(640, playerY)    # Land if dead (To look cleaner)
        elif playerY == 800:
            deadMan = True
            deathAnimations[selectedCharacter].display(640, playerY)    # Display the death animation


def checkConditions():
    global playerWon, gameMode, immune, immuneTimer, winTimer, deadAnimTimer, level2Locked, level3Locked
    if totalDistancePixels <= -29760:    # If statements checking conditions, checking if player travelled the amount of pixels to win
        playerWon = True
    if immune and immuneTimer < 300:     # Giving the player an immunity timer in the beginning of the level
        immuneTimer += 1
    elif immuneTimer == 300:
        immune = False
        immuneTimer = 0
    if playerWon:    # Checking if the player won, if they did sends them to the winPage
        winTimer += 1
        if winTimer == 135:
            gameMode = "winPage"
            winTimer = 0
        if level == 1:
            level2Locked = False
        else:
            level3Locked = False
    if deadMan:    # Checking if player is dead, if so send them to the gameOver page
        deadAnimTimer += 1
        if deadAnimTimer == 45:
            gameMode = "gameOver"
            deadAnimTimer = 0
        if bombDeath and deadAnimTimer < 15:
            explosionAnimation.display(600, 700)


def checkCollisions():
    # Function that is responsible for checking any collisions between the player and lasers, coins, or bombs
    global playerDead, coinsCollected, staticCoinPositions, bombPositions, bombDeath
    for i in range(len(laserPositions)):    # Looping for the amount of indexes in laserPositions list
        laserHitbox = Rect(laserPositions[i][0], laserPositions[i][1], 32, 305)    # Initializing the hit box of the laser
        if playerHitbox.colliderect(laserHitbox) and not immune:    # Checking for collision with the player and laser
            playerDead = True
            if not soundEffectsMuted:
                laserDeath.play()
            break
    for i in range(len(bombPositions)):    # Looping for the amount of indexes in bombPositions list
        bombHitbox = Rect(bombPositions[i][0], bombPositions[i][1], 100, 100)    # Initializing bomb hitbox
        if playerHitbox.colliderect(bombHitbox) and not immune:    # Checking for collision with bomb
            playerDead = True
            if not soundEffectsMuted:
                explosionSound.play()
            bombDeath = True
            del bombPositions[i]
            break
    for i in range(len(staticCoinPositions)):    # Looping for the amount of indexes in staticCoinPositions list
        coinHitbox = Rect(staticCoinPositions[i][0], staticCoinPositions[i][1], 50, 50)    # initializing static coin hitbox
        if playerHitbox.colliderect(coinHitbox):    # Checking for collision with static coin and player
            coinsCollected += 1
            if not soundEffectsMuted:    # If the sound effects arent muted, playing the coin sound
                coinCollect.play()
            del staticCoinPositions[i]
            break
    for i in range(len(dynamicCoinPositions)):    # Looping for the amount of indexes in dynamicCoinPositions list
        coinHitbox = Rect(dynamicCoinPositions[i][0], dynamicCoinPositions[i][1], 50, 50)    # Initializing dynamic coin hitbox
        if playerHitbox.colliderect(coinHitbox):    # Checking for collision with player and dynamic coin
            coinsCollected += 1
            if not soundEffectsMuted:
                coinCollect.play()
            del dynamicCoinPositions[i]
            break


def createCoins():
    # Function that is responsible for the creation of the coins within the levels.
    global staticCoinPositions, dynamicCoinPositions
    staticCoinPositions.clear()    # Clearing the lists to be safe, also fo runs after the first one
    dynamicCoinPositions.clear()
    for i in range(randint(7, 11)):    # Generating static coins
        xpos = randint(1260, 29660)    # Generating random X for static coin
        ypos = randint(25, 770)    # Generating random y for static coin
        staticCoinPositions.append([xpos, ypos])
    for i in range(randint(2, 5)):    # Generating dynamic coins
        xpos = randint(1260, 29660)
        originalypos = randint(350, 700)     # Generating random y for original dynamic coin
        ypos = randint(225, 570)
        dynamicCoinPositions.append([xpos, ypos, originalypos, 3])


def createBombs():
    # Function that is responsible for the creation of the bombs within the levels.
    global bombPositions
    bombPositions.clear()    # Clearing the list to be safe, also for runs after the first one
    for i in range(randint(3, 5)):
        xpos = randint(1260, 29660)    # Generating random X position
        bombPositions.append([xpos, 925])    # Appending the random xpos but all with the same Y so the bomb is on the ground


def drawBombs():
    # Function that is responsible for "drawing" bombs on the levels.
    global bombPositions
    for i in range(len(bombPositions)):
        screen.blit(bombImage, (bombPositions[i][0], bombPositions[i][1]))    # Generating the bomb at the position of the list
        bombPositions[i][0] -= scrollSpeed


def drawCoins():
    # Function that is responsible for "drawing" coins on the levels.
    global staticCoinPositions, dynamicCoinPositions
    for i in range(len(staticCoinPositions)):    # The loop is drawing the coins at random positions according to what we appended earlier to the staticCoinsPositions list
        coinAnimation.display(staticCoinPositions[i][0], staticCoinPositions[i][1])
        staticCoinPositions[i][0] -= scrollSpeed
    for i in range(len(dynamicCoinPositions)):    # Displaying the animated dynamic coin based off the positions appended earlier
        coinAnimation.display(dynamicCoinPositions[i][0], dynamicCoinPositions[i][1])
        if dynamicCoinPositions[i][1] < dynamicCoinPositions[i][2] - 200 or dynamicCoinPositions[i][1] > dynamicCoinPositions[i][2] + 200:
            dynamicCoinPositions[i][3] = -dynamicCoinPositions[i][3]
        dynamicCoinPositions[i][1] += dynamicCoinPositions[i][3]
        dynamicCoinPositions[i][0] -= scrollSpeed

    coinAnimation.display(1720, 50)    # Displaying the coin sprite
    coinsText = nebulaFont.render(str(coinsCollected), True, (255, 255, 255))
    screen.blit(coinsText, (1800, 50))


def createLasers():
    # Function that is responsible for the creation of the lasers within the levels.
    global laserPositions
    laserPositions.clear()    # Clearing the list to be safe, also for runs after the first one
    for i in range(8 + level * 3):
        xpos = randint(1260, 29660)    # We don't want a laser within the first 300 pixels and since 29760 is the end, we want the last laser at least 100 pixels before the end
        ypos = randint(25, 770)    # Difference between sprite height and laser height is 30 so 800 - 30
        laserPositions.append([xpos, ypos])


def drawLasers():
    # Function that is responsible for "drawing" lasers on the levels.
    global laserPositions
    for i in range(len(laserPositions)):
        if laserPositions[i][0] < 1750 and not immune:    # Doesn't draw the laser if you are immune, only draws when immunity expires
            screen.blit(laserOn, (laserPositions[i][0], laserPositions[i][1]))
        else:
            screen.blit(laserOff, (laserPositions[i][0], laserPositions[i][1]))
        laserPositions[i][0] -= scrollSpeed


def displayCoinsInAccount():
    # Function that is responsible for displaying the amount of coins in your account.
    coinAnimation.display(1720, 50)    # Displaying the coin amount with the coin animated "shining"
    coinsText = nebulaFont.render(str(coinsInAccount), True, (255, 255, 255))
    screen.blit(coinsText, (1780, 45))


def drawShop():
    # Function that is responsible for "drawing" all of the things on the shop page.
    screen.blit(menuBackground, (0, 0))
    confetti()    # Displaying confetti in background
    screen.blit(shopTitle, titleRect)
    displayBackButton()
    if selectedCharacter == 0:    # Series of if statements showing the skins as locked or unlocked dependant on if you purchased it or not
        screen.blit(skin1Selected, skin1Rect)
    else:
        screen.blit(skin1ImageNormal, skin1Rect)
    if skin2Locked:
        screen.blit(skin2ImageLocked, skin2Rect)
    elif selectedCharacter == 1:
        screen.blit(skin2Selected, skin2Rect)
    else:
        screen.blit(skin2ImageNormal, skin2Rect)
    if skin3Locked:
        screen.blit(skin3ImageLocked, skin3Rect)
    elif selectedCharacter == 2:
        screen.blit(skin3Selected, skin3Rect)
    else:
        screen.blit(skin3ImageNormal, skin3Rect)


def drawGameOver():
    # Function that is responsible for "drawing" all of the things on the game over page.
    screen.blit(gameOverLevels, gameEndRect)
    coinsCollectedText = nebulaFont.render("{} x{}".format(coinsCollected, coinMultiplier), True, (255, 255, 255))    # Displaying the amount of coins you collected during the level and with your prestige multiplier
    screen.blit(coinsCollectedText, (1220, 473))
    totalCoinsText = nebulaFont.render(str(coinsInAccount), True, (255, 255, 255))    # Amount of total coins you have in your account
    screen.blit(totalCoinsText, (1053, 525))
    screen.blit(continueButtonNormal, continueRect)    # Displaying continue button if you have enough coins
    screen.blit(returnToMenuButtonNormal, returnToMenuRect)    # Displaying return to menu button


def drawWinPage():
    # Function that is responsible for "drawing" all of the things on the win page.
    screen.blit(congratsScreen, gameEndRect)    # If level passed, draws the congrats screen
    coinsCollectedText = nebulaFont.render("{} x{}".format(coinsCollected, coinMultiplier), True, (255, 255, 255))    # Displaying the amount of coins you collected during the level and with your prestige multiplier
    screen.blit(coinsCollectedText, (1220, 473))
    totalCoinsText = nebulaFont.render(str(coinsInAccount), True, (255, 255, 255))    # Amount of total coins you have in your account
    screen.blit(totalCoinsText, (1053, 525))
    levelText = nebulaFont.render("{}".format(level), True, (255, 255, 255))
    screen.blit(levelText, (1270, 406))
    if level != 3:    # If you are on the final level, and since there can't be a next level button, this code draws a screen without the next level button
        screen.blit(nextLevelButtonNormal, nextLevelRect)
        screen.blit(returnToMenuButtonNormal, returnToMenuRect)
    else:
        screen.blit(returnToMenuButtonNormal, returnToMenuRectMiddle)


def drawArcadePage():
    # Function that is responsible for "drawing" all of the things on the arcade page.
    screen.blit(menuBackground, (0, 0))
    confetti()
    screen.blit(arcadeTitle, titleRect)
    displayBackButton()
    screen.blit(arcadeInformationImage, arcadeInformationRect)
    arcadeHighscoreText = nebulaFont.render("{:0>6}".format(arcadeHighscore), True, (255, 255, 255))    # Displaying highscore screen
    screen.blit(arcadeHighscoreText, (1030, 493))
    arcadeCoinsHighscoreText = nebulaFont.render("{:0>3}".format(arcadeCoinsHighscore), True, (255, 255, 255))
    screen.blit(arcadeCoinsHighscoreText, (1235, 549))
    screen.blit(playArcadeButtonNormal, playArcadeButtonRect)    # Displaying the play arcade button along with the rectangle to check for interaction


def arcadeInteraction():
    # Function that is responsible for the interactions on the arcade page. Displays hover images where needed and changes pages if clicked correctly
    global gameMode
    if playArcadeButtonRect.collidepoint(mx, my):    # If you press play, you play the arcade game mode
        if click:
            gameMode = "playArcade"
            setupArcade()
        else:
            screen.blit(playArcadeButtonHover, playArcadeButtonRect)


def insufficientFundsWarning():
    # Function that is responsible for displaying the warning/error if the user does not have enough coins to buy an item
    global insufficientFundsError
    insufficientText = nebulaFont.render(str(amountInsufficient), True, (255, 255, 255))
    insufficientTextRect = insufficientText.get_rect(center=(995, 600))
    screen.blit(insufficientFundsImage, insufficientFundsRect)    # Drawing the image and text for insufficient funds
    screen.blit(insufficientText, insufficientTextRect)
    insufficientFundsError -= 1


def setupArcade():
    # Function that is responsible for the placing obstacles for the arcade mode, resetting important values and setting up the speed and background
    global arcadeScrollSpeed, coinsCollected, arcadePlayerDead, coinsAdded, totalDistancePixels, backgroundX1, backgroundX2, bombDeath, deadMan, arcadePlayerWon
    if not musicMuted:
        mixer.music.pause()
    arcadeScrollSpeed = 11
    createArcadeLasers()
    createArcadeCoins()
    createArcadeBombs()
    coinsCollected = 0
    totalDistancePixels = 0
    backgroundX1 = 0
    backgroundX2 = background1.get_width()
    arcadePlayerDead = False
    deadMan = False
    coinsAdded = False
    bombDeath = False
    arcadePlayerWon = False


def createArcadeLasers():
    # Function that is responsible for the creation of the lasers within the arcade.
    global arcadeLaserPositions
    arcadeLaserPositions.clear()
    for i in range(330):
        xpos = randint(1260, 999990)  # We don't want a laser within the first 300 pixels and since 29760 is the end, we want the last laser at least 100 pixels before the end
        ypos = randint(25, 770)  # Difference between sprite height and laser height is 30 so 800 - 30
        arcadeLaserPositions.append([xpos, ypos])


def createArcadeCoins():
    # Function that is responsible for the creation of the coins within the arcade.
    global arcadeStaticCoinPositions, arcadeDynamicCoinPositions
    arcadeStaticCoinPositions.clear()
    arcadeDynamicCoinPositions.clear()
    for i in range(randint(150, 330)):  # Generating static coins
        xpos = randint(1260, 999990)  # Generating random X for static coin
        ypos = randint(25, 770)  # Generating random y for static coin
        arcadeStaticCoinPositions.append([xpos, ypos])
    for i in range(randint(20, 50)):  # Generating dynamic coins
        xpos = randint(1260, 999990)
        originalypos = randint(350, 700)  # Generating random y for original dynamic coin
        ypos = randint(225, 570)
        arcadeDynamicCoinPositions.append([xpos, ypos, originalypos, 3])


def createArcadeBombs():
    # Function that is responsible for the creation of the bombs within the arcade.
    global arcadeBombPositions
    arcadeBombPositions.clear()
    for i in range(randint(3, 5)):
        xpos = randint(1260, 999990)  # Generating random X position
        arcadeBombPositions.append([xpos, 925])  # Appending the random xpos but all with the same Y so the bomb is on the ground


def drawArcadeLasers():
    # Function that is responsible for "drawing" lasers on the arcade levels.
    global arcadeLaserPositions
    for i in range(len(arcadeLaserPositions)):
        if arcadeLaserPositions[i][0] < 1750 and not immune:  # Doesn't draw the laser if you are immune, only draws when immunity expires
            screen.blit(laserOn, (arcadeLaserPositions[i][0], arcadeLaserPositions[i][1]))
        else:
            screen.blit(laserOff, (arcadeLaserPositions[i][0], arcadeLaserPositions[i][1]))
        arcadeLaserPositions[i][0] -= arcadeScrollSpeed


def drawArcadeCoins():
    # Function that is responsible for "drawing" coins on the arcade levels.
    global arcadeStaticCoinPositions, arcadeDynamicCoinPositions
    for i in range(len(arcadeStaticCoinPositions)):  # The loop is drawing the coins at random positions according to what we appended earlier to the staticCoinsPositions list
        coinAnimation.display(arcadeStaticCoinPositions[i][0], arcadeStaticCoinPositions[i][1])
        arcadeStaticCoinPositions[i][0] -= arcadeScrollSpeed
    for i in range(len(arcadeDynamicCoinPositions)):  # Displaying the animated dynamic coin based off the positions appended earlier
        coinAnimation.display(arcadeDynamicCoinPositions[i][0], arcadeDynamicCoinPositions[i][1])
        if arcadeDynamicCoinPositions[i][1] < arcadeDynamicCoinPositions[i][2] - 200 or arcadeDynamicCoinPositions[i][1] > arcadeDynamicCoinPositions[i][2] + 200:
            arcadeDynamicCoinPositions[i][3] = -arcadeDynamicCoinPositions[i][3]
        arcadeDynamicCoinPositions[i][1] += arcadeDynamicCoinPositions[i][3]
        arcadeDynamicCoinPositions[i][0] -= arcadeScrollSpeed

    coinAnimation.display(1720, 50)  # Displaying the coin sprite
    coinsText = nebulaFont.render(str(coinsCollected), True, (255, 255, 255))
    screen.blit(coinsText, (1800, 45))


def drawArcadeBombs():
    # Function that is responsible for "drawing" bombs on the arcade levels.
    global arcadeBombPositions
    for i in range(len(arcadeBombPositions)):
        screen.blit(bombImage, (arcadeBombPositions[i][0], arcadeBombPositions[i][1]))  # Generating the bomb at the position of the list
        arcadeBombPositions[i][0] -= arcadeScrollSpeed


def moveArcadeScene():
    # Function that is responsible for "drawing" the scene and moving it.
    global backgroundX1, backgroundX2, arcadeScrollSpeed, totalDistancePixels, arcadeScore
    screen.blit(background1, (backgroundX1, 0))
    screen.blit(background2, (backgroundX2, 0))
    if not arcadePlayerDead:
        if totalDistancePixels > -1000000:  # If we haven't reached the end of the level (4 times through the background - half of the screen size)
            backgroundX1 -= arcadeScrollSpeed
            backgroundX2 -= arcadeScrollSpeed
            totalDistancePixels -= arcadeScrollSpeed
    if backgroundX1 <= -background1.get_width():    # Resetting the background to its original position if it is fully off screen
        backgroundX1 = backgroundX2 + background1.get_width()
    if backgroundX2 <= -background2.get_width():
        backgroundX2 = backgroundX1 + background2.get_width()
    arcadeScrollSpeed = 11 + -totalDistancePixels // 27760
    arcadeScore = -totalDistancePixels


def moveArcadePlayer():
    # Function that is responsible for movement and display of the character within the arcade mode
    global verticalVelocity, playerY, gameMode, deadMan
    # Moving the player
    if totalDistancePixels <= -999690:    # 999690 is going through 1 level 33 times, making arcade fun but challenging
        if playerY > 800:
            playerY = 800
            verticalVelocity = 0
        verticalVelocity += gravity
    else:
        if not arcadePlayerDead and not arcadePlayerWon:
            if playerY > 800:
                playerY = 800
                verticalVelocity = 0
            elif playerY < 25:
                playerY = 25
            if playerY < 800:
                verticalVelocity += gravity
            if flying and totalDistancePixels > -999900:
                verticalVelocity = jumpSpeed
        elif arcadePlayerDead:
            verticalVelocity += gravity
            if playerY > 800:
                playerY = 800
                verticalVelocity = 0
    playerY += verticalVelocity

    # Displaying the animations
    if not arcadePlayerDead:
        if flying:
            if playerY > 700:
                jumpAnimations[selectedCharacter].display(640, playerY)
            else:
                flyAnimations[selectedCharacter].display(640, playerY)
        else:
            if totalDistancePixels > -999990 and playerY == 800:
                runAnimations[selectedCharacter].display(640, playerY)
            elif arcadePlayerWon:
                winAnimations[selectedCharacter].display(640, playerY)
            else:
                landAnimations[selectedCharacter].display(640, playerY)
    else:
        if playerY < 800:
            landAnimations[selectedCharacter].display(640, playerY)
        elif playerY == 800:
            deadMan = True
            deathAnimations[selectedCharacter].display(640, playerY)


def checkArcadeCollisions():
    # Function that is responsible checking for any collision between the player and coins, lasers, or bombs within the arcade mode
    global arcadePlayerDead, coinsCollected, bombDeath
    for i in range(len(arcadeLaserPositions)):  # Looping for the amount of indexes in arcadeLaserPositions list
        laserHitbox = Rect(arcadeLaserPositions[i][0], arcadeLaserPositions[i][1], 32, 305)  # Initializing the hit box of the laser
        if playerHitbox.colliderect(laserHitbox) and not immune:  # Checking for collision with the player and laser
            arcadePlayerDead = True
            if not soundEffectsMuted:
                laserDeath.play()
            break
    for i in range(len(arcadeBombPositions)):  # Looping for the amount of indexes in ArcadeBombPositions list
        bombHitbox = Rect(arcadeBombPositions[i][0], arcadeBombPositions[i][1], 100, 100)  # Initializing bomb hitbox
        if playerHitbox.colliderect(bombHitbox) and not immune:  # Checking for collision with bomb
            arcadePlayerDead = True
            if not soundEffectsMuted:
                explosionSound.play()
            bombDeath = True
            del arcadeBombPositions[i]
            break
    for i in range(len(arcadeStaticCoinPositions)):  # Looping for the amount of indexes in staticCoinPositions list
        coinHitbox = Rect(arcadeStaticCoinPositions[i][0], arcadeStaticCoinPositions[i][1], 50, 50)  # initializing static coin hitbox
        if playerHitbox.colliderect(coinHitbox):  # Checking for collision with static coin and player
            coinsCollected += 1
            if not soundEffectsMuted:
                coinCollect.play()
            del arcadeStaticCoinPositions[i]
            break
    for i in range(len(arcadeDynamicCoinPositions)):  # Looping for the amount of indexes in dynamicCoinPositions list
        coinHitbox = Rect(arcadeDynamicCoinPositions[i][0], arcadeDynamicCoinPositions[i][1], 50, 50)  # Initializing dynamic coin hitbox
        if playerHitbox.colliderect(coinHitbox):  # Checking for collision with player and dynamic coin
            coinsCollected += 1
            if not soundEffectsMuted:
                coinCollect.play()
            del arcadeDynamicCoinPositions[i]
            break


def checkArcadeConditions():
    # Function that is responsible for checking for a condition
    global arcadePlayerWon, gameMode, winTimer, deadAnimTimer
    if totalDistancePixels <= -1000000:  # If statements checking conditions, checking if player travelled the amount of pixels to win
        arcadePlayerWon = True
    if arcadePlayerWon:  # Checking if the player won, if they did sends them to the winPage
        winTimer += 1
        if winTimer == 135:
            gameMode = "arcadeWinPage"
            winTimer = 0
    if deadMan:  # Checking if player is dead, if so send them to the gameOver page
        deadAnimTimer += 1
        if deadAnimTimer == 45:
            gameMode = "arcadeGameOver"
            deadAnimTimer = 0
        if bombDeath and deadAnimTimer < 15:
            explosionAnimation.display(600, 700)


def drawArcadeGameOver():
    # Function that is responsible for "drawing" the game over screen when dying in the arcade level.
    screen.blit(gameOverArcade, gameEndRect)
    coinsCollectedText = nebulaFont.render("{} x{}".format(coinsCollected, coinMultiplier), True, (255, 255, 255))  # Displaying the amount of coins you collected during the level and with your prestige multiplier
    screen.blit(coinsCollectedText, (1220, 473))
    totalCoinsText = nebulaFont.render(str(coinsInAccount), True, (255, 255, 255))  # Amount of total coins you have in your account
    screen.blit(totalCoinsText, (1053, 525))
    scoreText = nebulaFont.render("{:0>6}".format(arcadeScore), True, (255, 255, 255))
    screen.blit(scoreText, (850, 421))
    screen.blit(playAgainButtonNormal, playAgainRect)  # Displaying continue button if you have enough coins
    screen.blit(returnToMenuButtonNormal, returnToMenuRect)  # Displaying return to menu button1


def checkArcadeScore():
    # Function that is responsible for checking if a new highscore has been set, both for coins and for the actual score
    global arcadeHighscore, arcadeCoinsHighscore
    if arcadeScore > arcadeHighscore:    # Displaying a new high score if previous high score is beaten
        arcadeHighscore = arcadeScore
    if coinsCollected > arcadeCoinsHighscore:    # Displaying a new coin score if previous high score is beaten
        arcadeCoinsHighscore = coinsCollected


def arcadeGameOverInteraction():
    # Function that is responsible for the interaction with the arcade's game over page
    global gameMode, coinsAdded, coinsInAccount
    if not coinsAdded:
        coinsInAccount += coinsCollected * coinMultiplier    # Adding new coins collected into total
        coinsAdded = True
        checkArcadeScore()
    if playAgainRect.collidepoint(mx, my):    # Checking for collision with the play again button
        if click:
            setupArcade()
            gameMode = "playArcade"
        else:
            screen.blit(playAgainButtonHover, playAgainRect)
    if returnToMenuRect.collidepoint(mx, my):    # Checking if mouse collides with return to menu button returning you to menu
        if click:
            gameMode = "menu"
        else:
            screen.blit(returnToMenuButtonHover, returnToMenuRect)


def drawArcadeWinPage():
    # Function that is responsible for "drawing" the win page when winning in the arcade level.
    screen.blit(arcadeWinPage, gameEndRect)
    coinsCollectedText = nebulaFont.render("{} x{}".format(coinsCollected, coinMultiplier), True, (255, 255, 255))  # Displaying the amount of coins you collected during the level and with your prestige multiplier
    screen.blit(coinsCollectedText, (1220, 531))
    totalCoinsText = nebulaFont.render(str(coinsInAccount), True, (255, 255, 255))  # Amount of total coins you have in your account
    screen.blit(totalCoinsText, (1053, 584))
    scoreText = nebulaFont.render("{:0>6}".format(arcadeScore), True, (255, 255, 255))
    screen.blit(scoreText, (860, 481))
    screen.blit(returnToMenuButtonNormal, arcadeReturnRectMiddle)


def arcadeWinPageInteraction():
    # Function that is responsible for the interaction with the arcade's win page
    global gameMode
    if arcadeReturnRectMiddle.collidepoint(mx, my):    # Returning you to menu
        if click:
            gameMode = "menu"
        else:
            screen.blit(returnToMenuButtonHover, arcadeReturnRectMiddle)


def displayArcadeScore():
    # Function that is responsible for displaying the arcade score
    arcadeScoreText = nebulaFont.render("{:0>6}".format(arcadeScore), True, (255, 255, 255))
    screen.blit(arcadeScoreText, (50, 50))    # Displaying your score while in the arcade


def settingInteraction():
    # Function that is responsible for the interaction with the settings page
    global prestigeAlready, coinsInAccount, coinMultiplier, selectedCharacter, skin2Locked, skin3Locked, level2Locked, level3Locked, insufficientFundsError, amountInsufficient, showFPS, soundEffectsMuted, musicMuted
    if prestigeRect.collidepoint(mx, my):
        if not prestigeAlready:
            if click and coinsInAccount >= 500:    # Checking if you have enough coins for prestige, if you do completely resets account but gives you a coin multiplier
                coinsInAccount -= 500
                coinMultiplier = 5
                selectedCharacter = 0
                skin2Locked = True
                skin3Locked = True
                level2Locked = True
                level3Locked = True
                prestigeAlready = True
            elif click and coinsInAccount < 500:    # If you don't have enough coins, it will tell you the amount you need and make no changes to the prestige but
                insufficientFundsError = 165
                amountInsufficient = 500 - coinsInAccount
            elif mb[0]:
                screen.blit(prestigeButtonPressed, prestigeRect)
            else:
                screen.blit(prestigeButtonHover, prestigeRect)
    if fpsCheckRect.collidepoint(mx, my):    # Making show FPS button interactive (Showing and hiding FPS)
        if not showFPS:
            if click:
                showFPS = True
            else:
                screen.blit(checkHover, fpsCheckRect)
    if fpsUncheckRect.collidepoint(mx, my):
        if showFPS:
            if click:
                showFPS = False
            else:
                screen.blit(uncheckHover, fpsUncheckRect)
    if soundEffectsUnmuteRect.collidepoint(mx, my):    # Making sound effects button interactive
        if soundEffectsMuted:
            if click:
                soundEffectsMuted = False    # If the sound effects button is muted and you check it off, it will unmute it
            else:
                screen.blit(unmuteHover, soundEffectsUnmuteRect)
    if soundEffectsMuteRect.collidepoint(mx, my):
        if not soundEffectsMuted:
            if click:
                soundEffectsMuted = True
            else:
                screen.blit(muteHover, soundEffectsMuteRect)
    if musicUnmuteRect.collidepoint(mx, my):    # If the music button is muted and you check it off, it will unmute it
        if musicMuted:
            if click:
                musicMuted = False
                mixer.music.unpause()    # If any music was paused it will now play
            else:
                screen.blit(unmuteHover, musicUnmuteRect)
    if musicMuteRect.collidepoint(mx, my):
        if not musicMuted:    # If music is not muted and you check it, it will mute the music
            if click:
                musicMuted = True
                mixer.music.pause()    # If any music was playing, it will now pause
            else:
                screen.blit(muteHover, musicMuteRect)


def drawSettings():
    # Function that is responsible for "drawing" all of the things on the settings page.
    screen.blit(menuBackground, (0, 0))    # Drawing settings page
    confetti()
    screen.blit(settingsTitle, titleRect)
    screen.blit(settingsPageImage, settingsPageImageRect)

    if showFPS:    # If you have show fps on, it will draw a box with a check in it
        screen.blit(checkSelected, fpsCheckRect)
    else:
        screen.blit(checkNormal, fpsCheckRect)
    if not showFPS:    # If you have show fps off, it will draw a box with a uncheck symbol in it
        screen.blit(uncheckSelected, fpsUncheckRect)
    else:
        screen.blit(uncheckNormal, fpsUncheckRect)

    if not soundEffectsMuted:
        screen.blit(unmuteSelected, soundEffectsUnmuteRect)    # Drawing a unmute icon if sound effects are not muted and selected
    else:
        screen.blit(unmuteNormal, soundEffectsUnmuteRect)
    if soundEffectsMuted:    # If the sound effects are muted, use the muted icon
        screen.blit(muteSelected, soundEffectsMuteRect)
    else:
        screen.blit(muteNormal, soundEffectsMuteRect)

    if not musicMuted:    # Drawing a mute or unmute icon dependant on if the music is muted or unmuted
        screen.blit(unmuteSelected, musicUnmuteRect)
    else:
        screen.blit(unmuteNormal, musicUnmuteRect)
    if musicMuted:
        screen.blit(muteSelected, musicMuteRect)
    else:
        screen.blit(muteNormal, musicMuteRect)

    if not prestigeAlready:    # Displaying a button dependant on if you are prestige already or not
        screen.blit(prestigeButtonNormal, prestigeRect)
    else:
        screen.blit(prestigeMaster, prestigeRect)
    displayBackButton()


def displayFPS():
    # Function that is responsible for displaying the frames per second in the bottom right corner
    fps = int(myClock.get_fps())
    fpsText = nebulaFont.render(str(fps), True, (255, 255, 255))
    screen.blit(plateNormal, (50, 962))
    screen.blit(fpsText, (67, 981))


while running:    # Main loop of the game, nearly all functions are called on from here
    click = False
    flying = False
    for evt in event.get():
        if evt.type == QUIT:
            running = False
            writeData()
        if evt.type == MOUSEBUTTONDOWN and evt.button == 1:
            click = True
    keys = key.get_pressed()    # Getting the keys pressed, the mouse positions, and the mouse buttons that are pressed
    mb = mouse.get_pressed()
    mx, my = mouse.get_pos()
    playerHitbox = Rect(700, playerY + 35, 110, 195)    # Average player hitbox dimensions
    if keys[K_SPACE] and not playerWon:    # If you haven't won and you are pressing space, the character will fly (flying being true will activate the movePlayer part responsible for vertical lift)
        flying = True
    if gameMode == "menu":    # If the page is menu, draw it along with allowing interaction, and displaying coins
        if not mixer.music.get_busy() and not musicMuted:
            mixer.music.unpause()    # If the music is not muted, this line lets it play
        drawMenu()
        menuInteraction()
        displayCoinsInAccount()
    elif gameMode == "levelsPage":    # If the page is on the levels page, draw the levels page along with the interaction
        drawLevelsPage()
        levelsPageInteraction()
    elif gameMode == "playGame":    # If the page is playgame, scroll the background along with moving the character
        moveScene()
        movePlayer()
        if not playerDead:    # If the player is not dead, continue to draw the lasers, coins, bombs, and check for collisions and conditions
            drawLasers()
            drawCoins()
            drawBombs()
            checkCollisions()
        checkConditions()
    elif gameMode == "gameOver":    # Calling all of the functions needed for the level's game over page
        drawGameOver()
        if insufficientFundsError == 0:    # If there is no error then you could interact
            gameOverInteraction()
        else:
            insufficientFundsWarning()    # If there is an error then the function that displays the error is called upon
    elif gameMode == "arcadeMode":    # Calling all of the functions needed for the arcade page (not the game but the page before it)
        drawArcadePage()
        arcadeInteraction()
    elif gameMode == "playArcade":    # Calling all of the functions needed for the arcade game
        moveArcadeScene()
        moveArcadePlayer()
        if not arcadePlayerDead:    # If the player is not dead then the score is displayed, lasers, bombs, and coins are drawn, and we check for collisions (All done through individual functions)
            displayArcadeScore()
            drawArcadeLasers()
            drawArcadeCoins()
            drawArcadeBombs()
            checkArcadeCollisions()
        checkArcadeConditions()
    elif gameMode == "arcadeGameOver":    # Calling all of the functions needed for the arcade's game over page
        drawArcadeGameOver()
        arcadeGameOverInteraction()
    elif gameMode == "arcadeWinPage":    # Calling all of the functions needed for the arcade's win page
        drawArcadeWinPage()
        arcadeWinPageInteraction()
    elif gameMode == "shop":    # Calling all of the functions needed for the shop page
        drawShop()
        if insufficientFundsError == 0:    # If there is no error then you could interact
            shopInteraction()
        else:
            insufficientFundsWarning()    # If there is an error then the function that displays the error is called upon
        displayCoinsInAccount()
    elif gameMode == "settingsPage":    # Calling all of the functions needed for the settings page
        drawSettings()
        if insufficientFundsError == 0:    # If there is no error then you could interact
            settingInteraction()
        else:
            insufficientFundsWarning()
        displayCoinsInAccount()
    elif gameMode == "winPage":    # Calling all of the functions needed for the level's win page
        drawWinPage()
        winPageInteraction()
    if showFPS:    # If the fps is toggled to show, the function that shows the fps is called
        displayFPS()
    frame += 1    # Adding to the frame, used for my animation class
    myClock.tick(60)
    display.flip()
quit()
