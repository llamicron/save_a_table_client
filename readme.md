# Save a Table Client
This is a small script that detects when a physical switch is flipped, and when it is, POSTs it's state to the Save a Table site. the table ID will be stored in a file called `~/table_id`. This allows the code to be the same for every client, but they still need unique IDs.

I'm also logging every time a request is made. It's only a few extra lines of code, and I'll get some data.

# Usage
Put a file in this directory called `table_data`, containing this:
```json
{
	"number": 1,
	"floor": 6
}
```

And replace the proper values with the values for the table.
