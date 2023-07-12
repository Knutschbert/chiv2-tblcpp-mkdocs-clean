---
title: ATBLGameSession
type: class
aliases: ATBLGameSession
share: false

---

# ATBLGameSession





Inherits from AGameSession

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[ATBLGameSession]]**() |
| bool | **[[CanCancelMatchMaking]]**() const |
| bool | **[[CanStartMatchmaking]]**(bool bIsBackfill) const |
| bool | **[[CancelMatchmaking]]**() |
| void | **[[HandleMatchmakingCancelled]]**(FName MatchmadeSessionName, bool bSuccess) |
| void | **[[HandleMatchmakingComplete]]**(FName MatchmadeSessionName, bool bSuccess) |
| bool | **[[IsBusy]]**() const |
| bool | **[[IsMatchmaking]]**() |
| void | **[[OnServerListRefreshComplete]]**(bool bSuccess, EServerListType SearchType) |
| bool | **[[StartMatchmaking]]**(const TArray< [FMatchmakingQueue](/docs/SDK/Source/Classes/structFMatchmakingQueue.md) > & Queues) |
| bool | **[[StartServerListQuickMatch]]**(const [FServerFilterSetting](/docs/SDK/Source/Classes/structFServerFilterSetting.md) & Filters) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| int32 | **[[MaxNumExtraAdmins]]**  |
| FIsMatchmakingChanged | **[[OnIsMatchmakingChanged]]**  |
| FMatchmakingCancelled | **[[OnMatchmakingCancelled]]**  |
| FMatchmakingCompleted | **[[OnMatchmakingCompleted]]**  |
| FString | **[[ServerPassword]]**  |
| bool | **[[bIsCancellingMatchmaking]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200