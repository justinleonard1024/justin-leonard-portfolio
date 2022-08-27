/********************************
 * Custom Game Show
 * Resources.cs
 * Created by Justin Leonard
********************************/

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CustomGameShow
{
    class Resources
    {
        /*
         * Fields
         */
        public const int Round1 = 30;
        public const int Round2 = 60;
        public const int Round3 = 90;
        public const int RoundFinal = 120;
        public const int SettingsOffsetColor = 3;
        public const int SettingsOffsetMediaType = 17;
        public const int MediaEndTime = 21600;

        /*
         * Types
         */
        
        public enum ErrorCode
        {
            Generic,
            MissingMedia,
            NoAppSettings,
            InvalidContestantName,
            InvalidGameBoardColor,
            InvalidContestantColor,
            InvalidCategoryColor,
            InvalidMediaType
        }

        /*
         * Methods
         */
        
        public static string GetMediaDirectory()
        {
            // Get directory
            return Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData) + @"\Custom Game Show\Media\";
        }

        public static void Error(ErrorCode err, string data = "")
        {
            // Variables
            DialogResult result;

            // Check for error
            switch (err)
            {
                case ErrorCode.Generic:
                    // Error message
                    result = MessageBox.Show("An error has occured", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);

                    // Exit application
                    Environment.Exit(0);

                    // Exit
                    break;

                case ErrorCode.MissingMedia:
                    // Error message
                    result = MessageBox.Show("The media file " + data + " is missing", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);

                    // Exit application
                    Environment.Exit(0);

                    // Exit
                    break;

                case ErrorCode.NoAppSettings:
                    // Error message
                    result = MessageBox.Show("There are no application settings", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);

                    // Exit application
                    Environment.Exit(0);

                    // Exit
                    break;

                case ErrorCode.InvalidContestantName:
                    // Error message
                    result = MessageBox.Show("The contestant name " + data + " is invalid", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);

                    // Exit application
                    Environment.Exit(0);

                    // Exit
                    break;

                case ErrorCode.InvalidGameBoardColor:
                    // Error message
                    result = MessageBox.Show("The game board color " + data + " is invalid", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);

                    // Exit application
                    Environment.Exit(0);

                    // Exit
                    break;

                case ErrorCode.InvalidContestantColor:
                    // Error message
                    result = MessageBox.Show("The contestant text color " + data + " is invalid", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);

                    // Exit application
                    Environment.Exit(0);

                    // Exit
                    break;

                case ErrorCode.InvalidCategoryColor:
                    // Error message
                    result = MessageBox.Show("The category text color " + data + " is invalid", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);

                    // Exit application
                    Environment.Exit(0);

                    // Exit
                    break;

                case ErrorCode.InvalidMediaType:
                    // Error message
                    result = MessageBox.Show("The media type " + data + " is invalid", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);

                    // Exit application
                    Environment.Exit(0);

                    // Exit
                    break;

                // Other
                default:
                    // Exit
                    break;
            }
        }
    }
}
