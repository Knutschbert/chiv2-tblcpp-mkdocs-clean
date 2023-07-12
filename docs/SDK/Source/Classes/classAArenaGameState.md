---
title: AArenaGameState
type: class
aliases: AArenaGameState
share: false

---

# AArenaGameState





Inherits from [ATBLGameState](/docs/SDK/Source/Classes/classATBLGameState.md), AGameState, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

Inherited by [ALTSGameState](/docs/SDK/Source/Classes/classALTSGameState.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[AArenaGameState]]**() |
| void | **[[BroadcastRoundWonBy]]**(EFaction Winners) |
| void | **[[ClientPlayPodiumSequence]]**() |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| EFaction | **[[GetMatchPointFaction]]**() const |
| int32 | **[[GetNumberOfLivingPlayers]]**(EFaction Faction) |
| TArray< [AArenaPlayerState](/docs/SDK/Source/Classes/classAArenaPlayerState.md) * > | **[[GetPlayersAtStartOfRound]]**(EFaction Faction) |
| float | **[[GetPreCountdownTimeRemaining]]**() const |
| int32 | **[[GetRemainingLives]]**(EFaction Faction) |
| int32 | **[[GetRoundVictories]]**(EFaction Faction) const |
| bool | **[[IsMatchPointForFaction]]**(EFaction Faction) const |
| void | **[[SetRemainingLives]]**(EFaction Faction, int32 InRemainingLives) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[OnRep_LivingPlayers]]**() |
| void | **[[OnRep_RemainingLives]]**() |
| void | **[[OnRep_RoundVictories]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| int32 | **[[FinalLivesSetting]]**  |
| float | **[[MaxPlayersSetting]]**  |
| FOnPlayersAtStartOfRoundChanged | **[[OnAttackingPlayersAtStartOfRoundChanged]]**  |
| FOnPlayersAtStartOfRoundChanged | **[[OnDefendingPlayersAtStartOfRoundChanged]]**  |
| FOnNumLivingPlayersChanged | **[[OnNumLivingPlayersChanged]]**  |
| FOnRemainingLivesChanged | **[[OnRemainingLivesChanged]]**  |
| FOnRoundVictoriesChanged | **[[OnRoundVictoriesChanged]]**  |
| FOnRoundWonBy | **[[OnRoundWon]]**  |
| TArray< [FReplPodiumCharacterInfo](/docs/SDK/Source/Classes/structFReplPodiumCharacterInfo.md) > | **[[ReplicatedPodiumVictorInfos]]**  |
| [FReplVictoryPodium](/docs/SDK/Source/Classes/structFReplVictoryPodium.md) | **[[ReplicatedVictoryPodium]]**  |
| TArray< [FReplSequenceBinding](/docs/SDK/Source/Classes/structFReplSequenceBinding.md) > | **[[ReplicatedVictoryPodiumBindings]]**  |
| float | **[[RoundTimeLimitSetting]]**  |
| int32 | **[[RoundsSetting]]**  |
| int32 | **[[TeamLivesSetting]]**  |
| float | **[[TimeBetweenRoundsSetting]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200