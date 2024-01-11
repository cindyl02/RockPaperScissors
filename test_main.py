import main
from game_images import game_images


def test_run_program_scissors_and_rock(capfd, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2")
    monkeypatch.setattr("main.get_computer_choice", lambda: 0)
    main.run_program()
    out, err = capfd.readouterr()
    assert "You lose.\n" in out
    assert game_images[0] in out
    assert game_images[2] in out


def test_run_program_rock_and_scissors(capfd, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "0")
    monkeypatch.setattr("main.get_computer_choice", lambda: 2)
    main.run_program()
    out, err = capfd.readouterr()
    assert "You win!\n" in out
    assert game_images[0] in out
    assert game_images[2] in out


def test_run_program_rock_and_paper(capfd, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "0")
    monkeypatch.setattr("main.get_computer_choice", lambda: 1)
    main.run_program()
    out, err = capfd.readouterr()
    assert "You lose.\n" in out
    assert game_images[0] in out
    assert game_images[1] in out


def test_run_program_paper_and_rock(capfd, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1")
    monkeypatch.setattr("main.get_computer_choice", lambda: 0)
    main.run_program()
    out, err = capfd.readouterr()
    assert "You win!\n" in out
    assert game_images[0] in out
    assert game_images[1] in out


def test_run_program_paper_and_scissors(capfd, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1")
    monkeypatch.setattr("main.get_computer_choice", lambda: 2)
    main.run_program()
    out, err = capfd.readouterr()
    assert "You lose.\n" in out
    assert game_images[2] in out
    assert game_images[1] in out


def test_run_program_scissors_and_paper(capfd, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2")
    monkeypatch.setattr("main.get_computer_choice", lambda: 1)
    main.run_program()
    out, err = capfd.readouterr()
    assert "You win!\n" in out
    assert game_images[2] in out
    assert game_images[1] in out


def test_run_program_draw_rock_and_rock(capfd, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "0")
    monkeypatch.setattr("main.get_computer_choice", lambda: 0)
    main.run_program()
    out, err = capfd.readouterr()
    assert "It's a draw.\n" in out
    assert game_images[0] in out


def test_run_program_draw_paper_and_paper(capfd, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1")
    monkeypatch.setattr("main.get_computer_choice", lambda: 1)
    main.run_program()
    out, err = capfd.readouterr()
    assert "It's a draw.\n" in out
    assert game_images[1] in out


def test_run_program_draw_scissors_and_scissors(capfd, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2")
    monkeypatch.setattr("main.get_computer_choice", lambda: 2)
    main.run_program()
    out, err = capfd.readouterr()
    assert "It's a draw.\n" in out
    assert game_images[2] in out


def test_run_program_invalid_user_choice(capfd, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "3")
    main.run_program()
    out, err = capfd.readouterr()
    assert out == "Valid numbers are 0, 1, and 2. You lose.\n"


def test_run_program_invalid_user_choice_negative_number(capfd, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "-1")
    main.run_program()
    out, err = capfd.readouterr()
    assert out == "Valid numbers are 0, 1, and 2. You lose.\n"
