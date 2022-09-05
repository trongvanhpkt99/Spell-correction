using System;
using System.IO;
using System.Text;
using System.Collections.Generic;
using System.Threading.Tasks;
using Newtonsoft.Json;
using System.Linq;
using Newtonsoft.Json.Linq;

namespace Correction
{
    class Program
    {
        private static int EditDistDP(String str1, String str2)
        {
            int len1 = str1.Length;
            int len2 = str2.Length;

            int[,] DP = new int[2, len1 + 1];



            for (int i = 0; i <= len1; i++)
                DP[0, i] = i;


            for (int i = 1; i <= len2; i++)
            {
                for (int j = 0; j <= len1; j++)
                {
                    if (j == 0)
                        DP[i % 2, j] = i;
                    else if (str1[j - 1] == str2[i - 1])
                    {
                        DP[i % 2, j] = DP[(i - 1) % 2, j - 1];
                    }
                    else
                    {
                        DP[i % 2, j] = 1 + Math.Min(DP[(i - 1) % 2, j],
                                               Math.Min(DP[i % 2, j - 1],
                                                   DP[(i - 1) % 2, j - 1]));
                    }
                }
            }
            return DP[len2 % 2, len1];
        }
        public static async Task WriteToFile(string input, string file_input)
        {
            using StreamWriter file = new StreamWriter(file_input, append: true);
            await file.WriteLineAsync(input);
        }
        public static Dictionary<string, string[]> load_dict_from_jsonfile(string input_file)
        {
            Dictionary<string, string[]> dictionary = new Dictionary<string, string[]>();
            var dict = JObject.Parse(File.ReadAllText(input_file));
            foreach (var i in dict)
            {
                string[] values = i.Value.ToObject<string[]>();
                dictionary[i.Key] = values;
            }
            return dictionary;
        }
        public static void get_err(string input, Dictionary<string, string[]> dictionary, out Dictionary<string, List<string>> errs )
        {
            List<string> output = new List<string>();
            errs = new Dictionary<string, List<string>>();
            string[] k = input.Split(' ').ToArray();
            List<string> lines = new List<string>();
            lines.Add(input);
            
            foreach (var word in k)
            {
                foreach (var i in dictionary)
                {
                    if (word.ToLower().Trim().StartsWith(i.Key))
                    {
                        string cp_word = word.ToLower().Trim(',');
                        string sub = cp_word.Substring(i.Key.Length, cp_word.Length - i.Key.Length);
                        if (dictionary[i.Key].Contains(sub))
                        {
                            continue;
                        }
                        else
                        {
                            //Console.WriteLine(i.Key + sub);
                            output = lines;
                            int min_dp = sub.Length;
                            
                            foreach(var token in i.Value)
                            {
                                List<string> list_word = new List<string>();
                                int dp = EditDistDP(sub, token);
                                if (dp < min_dp)
                                {
                                    min_dp = dp;
                                    errs[word.Substring(0, i.Key.Length) + sub] = new List<string>();
                                }
                                if (dp == min_dp)
                                {
                                    List<string> list;
                                    if (errs.TryGetValue(word.Substring(0, i.Key.Length) + sub, out list))
                                        list.Add(word.Substring(0, i.Key.Length) + token);
                                    else
                                        errs.Add(word.Substring(0, i.Key.Length) + sub, new List<string>() { word.Substring(0, i.Key.Length) + token });
                                }

                            }
                            break;
                        }
                    }
                }
            }


            return ;
        }
        public static List<string> correct_err(string input, Dictionary<string, string[]> dictionary)
        {
            Dictionary<string, List<string>> errors= new Dictionary<string, List<string>>();
            get_err(input, dictionary,out errors);
            List<string> output = new List<string>();
            output.Add(input);
            foreach (var i in errors)
            {
                List<string> temp = new List<string>();
                foreach (var j in i.Value)
                {
                    
                    foreach(var k in output)
                    {
                        temp.Add(k.Replace(i.Key, j));
                        
                    }
                    
                }
                output = temp;

              
            }
            return output;
        }
        static void Main(string[] args)
        {

            Console.OutputEncoding = Encoding.UTF8;
            Console.InputEncoding = Encoding.UTF8;
            Dictionary<string, string[]> mydictionary = load_dict_from_jsonfile("Dictionary/dict_am.json");
            Dictionary<string, List<string>> errors = new Dictionary<string, List<string>>();
            var watch = System.Diagnostics.Stopwatch.StartNew();
            string input = "Thô Dục Túi 2, xã Dục Tú, huện Đôn9 Anh, Hà Nộ";
            List <string> output=correct_err(input, mydictionary);
            foreach(var line in output)
            {
                Console.WriteLine(line);
            }
            var elapsedMs = watch.ElapsedMilliseconds;
            Console.WriteLine("Task done after "+elapsedMs+"ms!!!");
        }
    }
}
