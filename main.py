import datetime
import os
from easydict import EasyDict

from Avalon.Game import Game
from Avalon.Player import Player


def main(config: EasyDict, evil_config: EasyDict):
    start_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    config.log_dir = os.path.join(config.log_dir, start_time)
    evil_config.log_dir = os.path.join(evil_config.log_dir, start_time)

    # 역할 리스트
    roles = [
        "Merlin", 
        "Percival", 
        "Loyal servant of arthur",
        "Loyal servant of arthur", 
        "Morgana", 
        "Assassin",
    ]

    # 플레이어 생성
    players = []
    for i, role in enumerate(roles):
        if role in ("Assassin", "Morgana"):
            cur_player = Player(id=i + 1, role=role, role_list=roles, config=evil_config)
        else:
            cur_player = Player(id=i + 1, role=role, role_list=roles, config=config)
        players.append(cur_player)

    # 게임 시작
    game = Game(players, config=config, logdir=config.log_dir)
    for player in game.players:
        player.set_game_belong_to(game)
    cur_game_result = game.start()
    print("Game result:", cur_game_result)


if __name__ == "__main__":
    # 직접 설정 지정
    config = EasyDict({
        "log_dir": "logs/good",
        "config_name": "ours_gpt",
        "evil_config_name": "baseline_gpt",
    })
    evil_config = EasyDict({
        "log_dir": "logs/evil",
        "config_name": "baseline_gpt",
    })

    # 실행
    main(config=config, evil_config=evil_config)
