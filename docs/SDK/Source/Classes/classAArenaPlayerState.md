---
title: AArenaPlayerState
type: class
aliases: AArenaPlayerState
share: false

---

# AArenaPlayerState





Inherits from [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md), APlayerState, [ITBLPlayerStateInterface](/docs/SDK/Source/Classes/classITBLPlayerStateInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[AArenaPlayerState]]**() |
| bool | **[[GetIsDeadAndOutOfLives]]**() |
| bool | **[[GetIsPartOfRound]]**() |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| int32 | **[[GetLivesLeft]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| FOnIsPartOfRoundChanged | **[[OnIsPartOfRoundChanged]]**  |
| FOnLivesLeftChanged | **[[OnLivesLeftChanged]]**  |
| FOnbIsDeadAndOutOfLivesChanged | **[[OnbIsDeadAndOutOfLivesChanged]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200