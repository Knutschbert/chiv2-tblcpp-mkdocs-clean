---
title: UKickVotingInstance
type: class
aliases: UKickVotingInstance
share: false

---

# UKickVotingInstance





Inherits from [UVotingInstance](/docs/SDK/Source/Classes/classUVotingInstance.md), UActorComponent, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) * | **[[GetKickTarget]]**() const |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| | **[[UKickVotingInstance]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [FReplicated_ATBLPayerState](/docs/SDK/Source/Classes/structFReplicated__ATBLPayerState.md) | **[[KickTarget]]**  |
| [FReplicated_EFaction](/docs/SDK/Source/Classes/structFReplicated__EFaction.md) | **[[KickTargetFaction]]**  |
| FName | **[[NoOption]]**  |
| FName | **[[YesOption]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[VoteKickBanTime]]**  |
| float | **[[VoteKickCooldown]]**  |
| int32 | **[[VoteKickMaxPercentageRequired]]**  |
| int32 | **[[VoteKickMinPercentageRequired]]**  |
| int32 | **[[VoteKickMinimumPlayers]]**  |
| EVoteKickType | **[[VoteKickType]]**  |
| int32 | **[[VoteKickUnanimousPlayerThreshold]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200