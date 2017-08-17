using System;
using CSGSI;
using CSGSI.Nodes;
using System.IO;

namespace CSGSI
{
    class Program
    {
        static GameStateListener gsl;
        static void Main(string[] args)
        {
            gsl = new GameStateListener(3000);
            gsl.NewGameState += new NewGameStateHandler(InGameState);
            if (!gsl.Start())
            {
                Console.WriteLine("Something went wrong - check if you have started the program as an admin");
                Console.ReadLine();
                Environment.Exit(0);
            }

            Console.WriteLine("CS:GO Game State Integration initialized");
            Console.WriteLine("Listening at port 3000\n");
            Console.WriteLine("-----------------------------------------------------------");
        }

        static void InGameState(GameState gs)
        {
            WriteStateToFile(gs);
            WriteConsoleOutput(gs);
        }

        static void WriteStateToFile(GameState gs)
        {
            string path = @"game_info";
            using (StreamWriter sw = File.CreateText(path))
            {
                sw.WriteLine(gs.Round.Bomb.ToString());                         //Bomb state
                sw.WriteLine(gs.Player.State.Health.ToString());                //Player health
                sw.WriteLine(gs.Player.State.Money.ToString());                 //Player money
                sw.WriteLine(gs.Player.Weapons.ActiveWeapon.Name.ToString());   //Active weapon name
            }

        }

        static void WriteConsoleOutput(GameState gs)
        {
            Console.WriteLine("Bomb state: " + gs.Round.Bomb.ToString());                               //Bomb state
            Console.WriteLine("Player health: " + gs.Player.State.Health.ToString());                   //Player health
            Console.WriteLine("Player money: " + gs.Player.State.Money.ToString());                     //Player money
            Console.WriteLine("Active weapon name: " + gs.Player.Weapons.ActiveWeapon.Name.ToString()); //Active weapon name
            Console.WriteLine("-----------------------------------------------------------");
        }
    }
}