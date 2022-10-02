VENV = venv
V_BIN = $(VENV)/bin


all: $(VENV)/chaos


$(VENV)/chaos: $(V_BIN)/python
	$(V_BIN)/pip install -e .


$(V_BIN)/%:
	python3 -m venv $(VENV)
	chmod +x $(V_BIN)/activate
	./$(V_BIN)/activate


clean:
	rm -rf *.egg-info
	rm -rf */__pycache__


fclean: clean
	rm -rf venv


.PHONY: all clean fclean
