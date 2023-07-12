---
title: UCinematicsComponent
type: class
aliases: UCinematicsComponent
share: false

---

# UCinematicsComponent





Inherits from UActorComponent

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[BindToPlayerState]]**(APlayerState * PlayerState) |
| [UCinematicState](/docs/SDK/Source/Classes/classUCinematicState.md) * | **[[GetCurrentState]]**() |
| FGameplayTag | **[[GetCurrentStateTag]]**() const |
| FGameplayTag | **[[GetCurrentUIState]]**() |
| [UCinematicState](/docs/SDK/Source/Classes/classUCinematicState.md) * | **[[GetState]]**(FGameplayTag Tag) |
| void | **[[GotoState]]**(FGameplayTag NextState) |
| void | **[[HandleGameCinematicStateChanged]]**(ECinematicGameState GameStateCinematicState) |
| void | **[[HandleMatchStateChanged]]**(FName MatchState) |
| bool | **[[IsInState]]**(FGameplayTag State) const |
| void | **[[SetUIState]]**(FGameplayTag UIState) |
| | **[[UCinematicsComponent]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TMap< FGameplayTag, TSoftClassPtr< [UCinematicState](/docs/SDK/Source/Classes/classUCinematicState.md) > > | **[[DefaultStates]]**  |
| FGameplayTag | **[[InitialState]]**  |
| FCinematicStateChanged | **[[OnCinematicStateChanged]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200