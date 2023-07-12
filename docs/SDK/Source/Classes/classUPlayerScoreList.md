---
title: UPlayerScoreList
type: class
aliases: UPlayerScoreList
share: false

---

# UPlayerScoreList





Inherits from UWidget

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[CheckForPlayerState]]**() |
| void | **[[OnInitialized]]**([ATBLPlayerController](/docs/SDK/Source/Classes/classATBLPlayerController.md) * PlayerOwner) |
| void | **[[OnPlayerLevelUpEvents]]**(const TArray< [FLevelUpResult](/docs/SDK/Source/Classes/structFLevelUpResult.md) > & LevelUpEvents) |
| void | **[[OnPlayerScoreEvent]]**([FScoreEventStruct](/docs/SDK/Source/Classes/structFScoreEventStruct.md) ScoreEvent) |
| | **[[UPlayerScoreList]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[PlayerStateReplicated]]**(APlayerState * PlayerState) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| FTimerHandle | **[[CheckForPlayerStateReplication]]**  |
| FGameplayTag | **[[DefaultTag]]**  |
| UWidget * | **[[HealingScoreWidget]]**  |
| float | **[[LevelUpLifeTime]]**  |
| float | **[[Lifetime]]**  |
| bool | **[[LoadedPlayerController]]**  |
| UWidget * | **[[ObjectiveScoreWidget]]**  |
| FOnGenerateLevelUpRow | **[[OnGenerateLevelUpRowEvent]]**  |
| FOnGenerateScoreRow | **[[OnGenerateRowEvent]]**  |
| TMap< [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) *, UWidget * > | **[[PlayerKilledWidgetMap]]**  |
| bool | **[[bSuccessfulPlayerStateReplicated]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200