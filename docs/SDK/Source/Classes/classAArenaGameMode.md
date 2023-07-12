---
title: AArenaGameMode
type: class
aliases: AArenaGameMode
share: false

---

# AArenaGameMode





Inherits from [ATBLGameMode_NativeBase](/docs/SDK/Source/Classes/classATBLGameMode__NativeBase.md), [ATBLGameMode](/docs/SDK/Source/Classes/classATBLGameMode.md), AGameMode

Inherited by [AJoustingGameMode](/docs/SDK/Source/Classes/classAJoustingGameMode.md), [ALTSGameMode](/docs/SDK/Source/Classes/classALTSGameMode.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[AArenaGameMode]]**() |
| void | **[[LoadPodiumCinematic]]**() |
| void | **[[ShowPodiumLevel]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AwardRoundVictoryAndEndRound]]**(EFaction Winners) |
| void | **[[PlayRoundFightCommanderVO]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| FArenaRoundEnd | **[[ArenaRoundEnd]]**  |
| FArenaRoundStart | **[[ArenaRoundStart]]**  |
| int32 | **[[FinalLives]]**  |
| int32 | **[[PreCountdownDelay]]**  |
| int32 | **[[RoundTimeLimit]]**  |
| int32 | **[[Rounds]]**  |
| int32 | **[[TeamLives]]**  |
| int32 | **[[TimeBetweenRounds]]**  |
| bool | **[[bClearHorsesPostRound]]**  |
| bool | **[[bClearWeaponsPostRound]]**  |
| bool | **[[bResetTaggedActorsPostRound]]**  |
| bool | **[[bUsePreCountdownForCustomizationLoading]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [UArenaGameModeSettings](/docs/SDK/Source/Classes/classUArenaGameModeSettings.md) * | **[[ArenaGameModeSettings]]**  |
| int32 | **[[CurrentRoundNumber]]**  |
| bool | **[[bMatchEndingMusicTrigger]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200