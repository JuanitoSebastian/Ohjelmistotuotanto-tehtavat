import Foundation

class TennisGame1: TennisGame {
    private let player1: String
    private let player2: String
    private var score1: Int
    private var score2: Int

    required init(player1: String, player2: String) {
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0
    }

    func wonPoint(_ playerName: String) {
        switch playerName {
        case player1:
            score1 += 1
        default:
            score2 += 1
        }
    }

    var score: String? {
        if tie {
            return score1 > 2 ? "Deuce" : "\(getPointsString(score1))-All"
        }

        if score1 < 4 && score2 < 4 {
            return "\(getPointsString(score1))-\(getPointsString(score2))"
        }

        return differenceInScore < 2 ? "Advantage \(playerWithHigherScore)" : "Win for \(playerWithHigherScore)"
    }
}


// MARK: - Private functions and variables
extension TennisGame1 {

    private func getPointsString(_ points: Int) -> String {
        switch points {
        case 0:
            return "Love"
        case 1:
            return "Fifteen"
        case 2:
            return "Thirty"
        default:
            return "Forty"
        }
    }

    private var tie: Bool {
        return score1 == score2
    }

    private var playerWithHigherScore: String {
        return score1 > score2 ? "player1" : "player2"
    }

    private var differenceInScore: Int {
        return abs(score1 - score2)
    }

}
