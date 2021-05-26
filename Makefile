all: clean
	@python3 -w ignore simulator.py simulator > /dev/null

clean:
	rm -f simulator > /dev/null

.PHONY: all clean