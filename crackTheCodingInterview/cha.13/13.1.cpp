#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include <queue>
using namespace std;


int tail(string file_name, unsigned int k)
{
  ifstream fin(file_name.c_str());
  if ( !fin.is_open() ) {
    cout << "ERROR: File " << file_name << " cannot open." << endl;
    return -1;
  }
  queue<string> last_k_lines;
  string line;
  while ( getline(fin, line) ) {
    if (last_k_lines.size() >= k) {
      last_k_lines.pop();
    }
    last_k_lines.push(line);
  }
  for ( unsigned int i = 0; i < k; i++ ) {
    cout << last_k_lines.front() << endl;
    last_k_lines.pop();
  }
  fin.close();
  return 0;
}


int main(int argc, char * argv[])
{
  if ( argc < 3 ) {
    cout << "ERROR: More arguments are required"
         << "Usage: " << argv[0] << " file_name line_count" << endl;
    return -1;
  }
  tail(static_cast<string>(argv[1]),
       static_cast<unsigned int>(atoi(argv[2])));
  return 0;
}
