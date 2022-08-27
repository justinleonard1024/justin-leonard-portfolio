/********************************
 * Super Stop N Buy
 * Global.cs
 * Created by Justin Leonard
 * < Other Names Omitted >
********************************/

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SuperStopNBuy
{
    class Global
    {
        // Variables
        public const string ConnectionString = "UID=< Omitted >;Password=< Omitted >;Server=sql9.freesqldatabase.com;Database=< Omitted >;Port=3306";
        public const string AccessToken = "< Omitted >";
        public const string AppName = "SuperStopNBuy";
        public const string AppKey = "< Omitted >";
        public const string AppDirectory = "/Items/";
        public const string AppExtension = ".png";

        public static string GetTemporaryDownloadPath()
        {
            // Return
            return Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData), "SuperStopNBuy\\");
        }

        public static void CreateTemporaryDownloadPath()
        {
            // Check if directory exists
            if (!Directory.Exists(GetTemporaryDownloadPath()))
            {
                // Create directory
                Directory.CreateDirectory(GetTemporaryDownloadPath());
            }
        }

        public static void DeleteTemporaryDownloadPath()
        {
            // Check if directory exists
            if (Directory.Exists(GetTemporaryDownloadPath()))
            {
                // Delete directory
                Directory.Delete(GetTemporaryDownloadPath(), true);
            }
        }
    }
}
