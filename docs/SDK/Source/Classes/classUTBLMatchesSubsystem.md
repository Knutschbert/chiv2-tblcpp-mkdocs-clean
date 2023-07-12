---
title: UTBLMatchesSubsystem
type: class
aliases: UTBLMatchesSubsystem
share: false

---

# UTBLMatchesSubsystem





Inherits from UGameInstanceSubsystem

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[UTBLMatchesSubsystem]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[MatchUpdate]]**() |
| void | **[[OnGameStateSetEvent]]**(AGameStateBase * GameState) |
| void | **[[OnMatchStateChanged]]**(FName NewMatchState) |
| void | **[[OnPS5MatchIdChanged]]**(const FString & MatchID) |
| void | **[[OnPS5MatchResponsiblePlayerUpdated]]**(FUniqueNetIdRepl Player) |
| void | **[[OnPostLoadMap]]**(UWorld * LoadedWorld) |
| void | **[[OnPreLoadMap]]**(const FString & MapName) |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200