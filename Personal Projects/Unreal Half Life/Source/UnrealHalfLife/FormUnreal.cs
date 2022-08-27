/********************************
 * Unreal Half Life
 * FormUnreal.cs
 * Created by Justin Leonard
********************************/

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Configuration;
using System.Reflection;
using System.Diagnostics;
using System.IO;

namespace UnrealHalfLife
{
    public partial class FormUnreal : Form
    {
        /*
         * Fields
         */
        private int settings_model, settings_texture, settings_shader, 
            settings_water, settings_shadow, settings_vsync;

        /*
         * Constructor
         */
        
        public FormUnreal()
        {
            InitializeComponent();
        }

        /*
         * Form Events
         */
        
        private void FormUnreal_Load(object sender, EventArgs e)
        {
            // Variables
            settings_model = 1;
            settings_texture = 0;
            settings_shader = 0;
            settings_water = 0;
            settings_shadow = 1;
            settings_vsync = 1;

            // Preset Update
            unreal_presetupdate();

            // Model Settings
            if(settings_model == 2)
            {
                // Low
                model_button_low.Checked = true;
            }
            else if (settings_model == 1)
            {
                // Medium
                model_button_medium.Checked = true;
            }
            else if (settings_model == 0)
            {
                // High
                model_button_high.Checked = true;
            }

            // Texture Settings
            if (settings_texture == 2)
            {
                // Low
                texture_button_low.Checked = true;
            }
            else if (settings_texture == 1)
            {
                // Medium
                texture_button_medium.Checked = true;
            }
            else if (settings_texture == 0)
            {
                // High
                texture_button_high.Checked = true;
            }

            // Shader Settings
            if (settings_shader == 2)
            {
                // Low
                shader_button_low.Checked = true;
            }
            else if (settings_shader == 1)
            {
                // Medium
                shader_button_medium.Checked = true;
            }
            else if (settings_shader == 0)
            {
                // High
                shader_button_high.Checked = true;
            }

            // Water Settings
            if (settings_water == 0)
            {
                // Low
                water_button_low.Checked = true;
            }
            else if (settings_water == 1)
            {
                // High
                water_button_high.Checked = true;
            }

            // Shadow Settings
            if (settings_shadow == 0)
            {
                // Low
                shadow_button_low.Checked = true;
            }
            else if (settings_shadow == 1)
            {
                // High
                shadow_button_high.Checked = true;
            }

            // Vsync Settings
            if (settings_vsync == 0)
            {
                // Off
                vsync_button_off.Checked = true;
            }
            else if (settings_vsync == 1)
            {
                // On
                vsync_button_on.Checked = true;
            }
        }

        /*
         * Button Events
         */
        
        private void model_button_low_CheckedChanged(object sender, EventArgs e)
        {
            if (model_button_low.Checked == true)
            {
                // Settings
                settings_model = 2;

                // Preset Update
                unreal_presetupdate();
            }
        }

        private void model_button_medium_CheckedChanged(object sender, EventArgs e)
        {
            if (model_button_medium.Checked == true)
            {
                // Settings
                settings_model = 1;

                // Preset Update
                unreal_presetupdate();
            }
        }

        private void model_button_high_CheckedChanged(object sender, EventArgs e)
        {
            if (model_button_high.Checked == true)
            {
                // Settings
                settings_model = 0;

                // Preset Update
                unreal_presetupdate();
            }
        }
		
        private void texture_button_low_CheckedChanged(object sender, EventArgs e)
        {
            if (texture_button_low.Checked == true)
            {
                // Settings
                settings_texture = 2;

                // Preset Update
                unreal_presetupdate();
            }
        }

        private void texture_button_medium_CheckedChanged(object sender, EventArgs e)
        {
            if (texture_button_medium.Checked == true)
            {
                // Settings
                settings_texture = 1;

                // Preset Update
                unreal_presetupdate();
            }
        }

        private void texture_button_high_CheckedChanged(object sender, EventArgs e)
        {
            if (texture_button_high.Checked == true)
            {
                // Settings
                settings_texture = 0;

                // Preset Update
                unreal_presetupdate();
            }
        }
		
        private void shader_button_low_CheckedChanged(object sender, EventArgs e)
        {
            if (shader_button_low.Checked == true)
            {
                // Settings
                settings_shader = 2;

                // Preset Update
                unreal_presetupdate();
            }
        }

        private void shader_button_medium_CheckedChanged(object sender, EventArgs e)
        {
            if (shader_button_medium.Checked == true)
            {
                // Settings
                settings_shader = 1;

                // Preset Update
                unreal_presetupdate();
            }
        }

        private void shader_button_high_CheckedChanged(object sender, EventArgs e)
        {
            if (shader_button_high.Checked == true)
            {
                // Settings
                settings_shader = 0;

                // Preset Update
                unreal_presetupdate();
            }
        }
		
        private void water_button_low_CheckedChanged(object sender, EventArgs e)
        {
            if (water_button_low.Checked == true)
            {
                // Settings
                settings_water = 0;

                // Preset Update
                unreal_presetupdate();
            }
        }

        private void water_button_high_CheckedChanged(object sender, EventArgs e)
        {
            if (water_button_high.Checked == true)
            {
                // Settings
                settings_water = 1;

                // Preset Update
                unreal_presetupdate();
            }
        }
		
        private void shadow_button_low_CheckedChanged(object sender, EventArgs e)
        {
            if (shadow_button_low.Checked == true)
            {
                // Settings
                settings_shadow = 0;

                // Preset Update
                unreal_presetupdate();
            }
        }

        private void shadow_button_high_CheckedChanged(object sender, EventArgs e)
        {
            if (shadow_button_high.Checked == true)
            {
                // Settings
                settings_shadow = 1;

                // Preset Update
                unreal_presetupdate();
            }
        }
		
        private void vsync_button_off_CheckedChanged(object sender, EventArgs e)
        {
            if (vsync_button_off.Checked == true)
            {
                // Settings
                settings_vsync = 0;
            }
        }

        private void vsync_button_on_CheckedChanged(object sender, EventArgs e)
        {
            if (vsync_button_on.Checked == true)
            {
                // Settings
                settings_vsync = 1;
            }
        }
		
        private void play_button_Click(object sender, EventArgs e)
        {
            // Path variables
            string path_1 = System.Environment.GetFolderPath(System.Environment.SpecialFolder.ProgramFilesX86);
            string path_2 = @"Steam\SteamApps\common\Half-Life 2\hl2.exe";
            string path_final = Path.Combine(path_1, path_2);

            if (!File.Exists(path_final))
            {
                MessageBox.Show("Half Life 2 not installed or executable missing.\nPlease install Half Life 2 to play.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            else
            {
                // Start Game
                unreal_game_start();

                // Exit App
                Application.Exit();
            }
        }
		
        private void preset_combobox_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (preset_combobox.Text == "Low")
            {
                // Settings
                settings_model = 2;
                settings_texture = 2;
                settings_shader = 2;
                settings_water = 0;
                settings_shadow = 0;

                // Buttons
                model_button_low.Checked = true;
                texture_button_low.Checked = true;
                shader_button_low.Checked = true;
                water_button_low.Checked = true;
                shadow_button_low.Checked = true;
            }
            else if (preset_combobox.Text == "Medium")
            {
                // Settings
                settings_model = 1;
                settings_texture = 1;
                settings_shader = 1;
                settings_water = 0;
                settings_shadow = 0;

                // Buttons
                model_button_medium.Checked = true;
                texture_button_medium.Checked = true;
                shader_button_medium.Checked = true;
                water_button_low.Checked = true;
                shadow_button_low.Checked = true;
            }
            else if (preset_combobox.Text == "High")
            {
                // Settings
                settings_model = 0;
                settings_texture = 0;
                settings_shader = 0;
                settings_water = 1;
                settings_shadow = 1;

                // Buttons
                model_button_high.Checked = true;
                texture_button_high.Checked = true;
                shader_button_high.Checked = true;
                water_button_high.Checked = true;
                shadow_button_high.Checked = true;
            }
        }

        /*
         * Methods
         */
        
        private void unreal_presetupdate()
        {
            // Preset Settings
            if (settings_model == 2 && settings_texture == 2 && settings_shader == 2 &&
                settings_water == 0 && settings_shadow == 0)
            {
                // Low
                preset_combobox.Text = "Low";
            }
            else if (settings_model == 1 && settings_texture == 1 && settings_shader == 1 &&
                settings_water == 0 && settings_shadow == 0)
            {
                // Medium
                preset_combobox.Text = "Medium";
            }
            else if (settings_model == 0 && settings_texture == 0 && settings_shader == 0 &&
                settings_water == 1 && settings_shadow == 1)
            {
                // High
                preset_combobox.Text = "High";
            }
            else
            {
                // None
                preset_combobox.Text = "None";
            }
        }
		
        private void unreal_config()
        {
            // Path
            string path_1 = System.Environment.GetFolderPath(System.Environment.SpecialFolder.ProgramFilesX86);
            string path_2 = @"Steam\SteamApps\common\Half-Life 2\hl2\unreal\_Assets\_dynamic\cfg\";
            string path_autoexec = path_2 + "autoexec.cfg";
            string path_config = path_2 + "unreal_cfg.cfg";
            string path_settings = path_2 + "unreal_settings.cfg";

            string path_final_autoexec = Path.Combine(path_1, path_autoexec);
            string path_final_config = Path.Combine(path_1, path_config);
            string path_final_settings = Path.Combine(path_1, path_settings);

            // Validate Files
            if (!File.Exists(path_final_autoexec))
            {
                FileStream file_autoexec = File.Create(path_final_autoexec);
                file_autoexec.Close();
            }

            if (!File.Exists(path_final_config))
            {
                FileStream file_config = File.Create(path_final_config);
                file_config.Close();
            }

            if (!File.Exists(path_final_settings))
            {
                FileStream file_settings = File.Create(path_final_settings);
                file_settings.Close();
            }

            // Configs
            string config_autoexec = "// Unreal Autoexec\r\n// Executes when the game starts\r\n// Created by Justin Leonard\r\n\r\n// Initial Setup\r\nexec unreal_cfg\r\n\r\n// End";
            string config_cfg = "// Unreal Config\r\n// Initial Setup\r\n// Created by Justin Leonard\r\n\r\n// Commands\r\ngl_clear 1\r\ncrosshair 1\r\nhud_draw_fixed_reticle 0\r\nsv_infinite_aux_power 1\r\nr_drawviewmodel 1\r\nmat_fullbright 0\r\nmat_drawTextureScale 0\r\nsv_unlockedchapters 15\r\n\r\n// Settings\r\nexec unreal_settings\r\n\r\n// End";

            // Main
            string config_main = "";
            string config_header = "// Unreal Game Settings\r\n// Set by the game launcher\r\n// Created by Justin Leonard\r\n\r\n";
            string config_footer = "\r\n// End";

            // Model Settings
            string config_model_low = "// Model Quality\r\n\r\n// Low\r\nr_rootlod 2\r\n\r\n// Medium\r\n//r_rootlod 1\r\n\r\n// High\r\n//r_rootlod 0\r\n";
            string config_model_medium = "// Model Quality\r\n\r\n// Low\r\n//r_rootlod 2\r\n\r\n// Medium\r\nr_rootlod 1\r\n\r\n// High\r\n//r_rootlod 0\r\n";
            string config_model_high = "// Model Quality\r\n\r\n// Low\r\n//r_rootlod 2\r\n\r\n// Medium\r\n//r_rootlod 1\r\n\r\n// High\r\nr_rootlod 0\r\n";

            // Texture Settings
            string config_texture_low = "\r\n\r\n\r\n// Texture Quality\r\n\r\n// Low\r\nmat_picmip 2\r\n\r\n// Medium\r\n//mat_picmip 1\r\n\r\n// High\r\n//mat_picmip 0\r\n";
            string config_texture_medium = "\r\n\r\n\r\n// Texture Quality\r\n\r\n// Low\r\n//mat_picmip 2\r\n\r\n// Medium\r\nmat_picmip 1\r\n\r\n// High\r\n//mat_picmip 0\r\n";
            string config_texture_high = "\r\n\r\n\r\n// Texture Quality\r\n\r\n// Low\r\n//mat_picmip 2\r\n\r\n// Medium\r\n//mat_picmip 1\r\n\r\n// High\r\nmat_picmip 0\r\n";

            // Shader Settings
            string config_shader_low = "\r\n\r\n\r\n// Shader Quality\r\n\r\n// Low\r\nmat_reducefillrate 1\r\n\r\n// Medium\r\n//mat_reducefillrate 1\r\n\r\n// High\r\n//mat_reducefillrate 0\r\n";
            string config_shader_medium = "\r\n\r\n\r\n// Shader Quality\r\n\r\n// Low\r\n//mat_reducefillrate 1\r\n\r\n// Medium\r\nmat_reducefillrate 1\r\n\r\n// High\r\n//mat_reducefillrate 0\r\n";
            string config_shader_high = "\r\n\r\n\r\n// Shader Quality\r\n\r\n// Low\r\n//mat_reducefillrate 1\r\n\r\n// Medium\r\n//mat_reducefillrate 1\r\n\r\n// High\r\nmat_reducefillrate 0\r\n";

            // Water Settings
            string config_water_low = "\r\n\r\n\r\n// Water Quality\r\n\r\n// Low\r\nr_waterforceexpensive 0\r\n\r\n// High\r\n//r_waterforceexpensive 1\r\n";
            string config_water_high = "\r\n\r\n\r\n// Water Quality\r\n\r\n// Low\r\n//r_waterforceexpensive 0\r\n\r\n// High\r\nr_waterforceexpensive 1\r\n";

            // Shadow Settings
            string config_shadow_low = "\r\n\r\n\r\n// Shadow Quality\r\n\r\n// Low\r\nr_shadowrendertotexture 0\r\n\r\n// High\r\n//r_shadowrendertotexture 1\r\n";
            string config_shadow_high = "\r\n\r\n\r\n// Shadow Quality\r\n\r\n// Low\r\n//r_shadowrendertotexture 0\r\n\r\n// High\r\nr_shadowrendertotexture 1\r\n";

            // Vsync Settings
            string config_vsync_off = "\r\n\r\n\r\n// Vsync\r\n\r\n// Off\r\nmat_vsync 0\r\n\r\n// On\r\n//mat_vsync 1\r\n";
            string config_vsync_on = "\r\n\r\n\r\n// Vsync\r\n\r\n// Off\r\n//mat_vsync 0\r\n\r\n// On\r\nmat_vsync 1\r\n";

            // Main Header
            config_main += config_header;

            // Model Settings
            if (settings_model == 2)
            {
                // Low
                config_main += config_model_low;
            }
            else if (settings_model == 1)
            {
                // Medium
                config_main += config_model_medium;
            }
            else if (settings_model == 0)
            {
                // High
                config_main += config_model_high;
            }

            // Texture Settings
            if (settings_texture == 2)
            {
                // Low
                config_main += config_texture_low;
            }
            else if (settings_texture == 1)
            {
                // Medium
                config_main += config_texture_medium;
            }
            else if (settings_texture == 0)
            {
                // High
                config_main += config_texture_high;
            }

            // Shader Settings
            if (settings_shader == 2)
            {
                // Low
                config_main += config_shader_low;
            }
            else if (settings_shader == 1)
            {
                // Medium
                config_main += config_shader_medium;
            }
            else if (settings_shader == 0)
            {
                // High
                config_main += config_shader_high;
            }

            // Water Settings
            if (settings_water == 0)
            {
                // Low
               config_main += config_water_low;
            }
            else if (settings_water == 1)
            {
                // High
                config_main += config_water_high;
            }

            // Shadow Settings
            if (settings_shadow == 0)
            {
                // Low
               config_main += config_shadow_low;
            }
            else if (settings_shadow == 1)
            {
                // High
                config_main += config_shadow_high;
            }

            // Vsync Settings
            if (settings_vsync == 0)
            {
                // Off
                config_main += config_vsync_off;
            }
            else if (settings_vsync == 1)
            {
                // On
                config_main += config_vsync_on;
            }

            // Main Footer
            config_main += config_footer;

            // Write to file
            File.WriteAllText(path_final_autoexec, config_autoexec);
            File.WriteAllText(path_final_config, config_cfg);
            File.WriteAllText(path_final_settings, config_main);
        }
		
        private void unreal_gameinfo_normal()
        {
            string path_1 = System.Environment.GetFolderPath(System.Environment.SpecialFolder.ProgramFilesX86);
            string path_2 = @"Steam\SteamApps\common\Half-Life 2\hl2\gameinfo.txt";
            string path_final = Path.Combine(path_1, path_2);
            string gameinfo = "\"GameInfo\"\r\n{\r\n	game 		\"HALF-LIFE 2\"\r\n	title 		\"HALF-LIFE\'\"\r\n	type		singleplayer_only\r\n	supportsvr	1\r\n\r\n	FileSystem\r\n	{\r\n		SteamAppId				220		// This will mount all the GCFs we need (240=CS:S, 220=HL2).\r\n		\r\n		//\r\n		// The code that loads this file automatically does a few things here:\r\n		//\r\n		// 1. For each \"Game\" search path, it adds a \"GameBin\" path, in <dir>\\bin\r\n		// 2. For each \"Game\" search path, it adds another \"Game\" path in front of it with _<langage> at the end.\r\n		//    For example: c:\\hl2\\cstrike on a french machine would get a c:\\hl2\\cstrike_french path added to it.\r\n		// 3. For the first \"Game\" search path, it adds a search path called \"MOD\".\r\n		// 4. For the first \"Game\" search path, it adds a search path called \"DEFAULT_WRITE_PATH\".\r\n		//\r\n\r\n		//\r\n		// Search paths are relative to the base directory, which is where hl2.exe is found.\r\n		//\r\n		// |gameinfo_path| points at the directory where gameinfo.txt is.\r\n		// We always want to mount that directory relative to gameinfo.txt, so\r\n		// people can mount stuff in c:\\mymod, and the main game resources are in\r\n		// someplace like c:\\program files\\valve\\steam\\steamapps\\half-life 2.\r\n		//\r\n		SearchPaths\r\n		{\r\n			// First, mount all user customizations.  This will search for VPKs and subfolders\r\n			// and mount them in alphabetical order.  The easiest way to distribute a mod is to\r\n			// pack up the custom content into a VPK.  To \"install\" a mod, just drop it in this\r\n			// folder.\r\n			//\r\n			// Note that this folder is scanned only when the game is booted.\r\n			game+mod			hl2/custom/*\r\n\r\n			// We search VPK files before ordinary folders, because most files will be found in\r\n			// VPK and we can avoid making thousands of file system calls to attempt to open files\r\n			// in folders where they don\'t exist.  (Searching a VPK is much faster than making an operating\r\n			// system call.)\r\n			game_lv				hl2/hl2_lv.vpk\r\n			game+mod			hl2/hl2_sound_vo_english.vpk\r\n			game+mod			hl2/hl2_pak.vpk\r\n			game				|all_source_engine_paths|hl2/hl2_textures.vpk\r\n			game				|all_source_engine_paths|hl2/hl2_sound_misc.vpk\r\n			game				|all_source_engine_paths|hl2/hl2_misc.vpk\r\n			platform			|all_source_engine_paths|platform/platform_misc.vpk\r\n\r\n			// Now search loose files.  We\'ll set the directory containing the gameinfo.txt file\r\n			// as the first \"mod\" search path (after any user customizations).  This is also the one\r\n			// that\'s used when writing to the \"mod\" path.\r\n			mod+mod_write+default_write_path		|gameinfo_path|.\r\n\r\n			// Add the HL2 directory as a game search path.  This is also where where writes\r\n			// to the \"game\" path go.\r\n			game+game_write		hl2\r\n\r\n			// Where the game\'s binaries are\r\n			gamebin				hl2/bin\r\n\r\n			// Last, mount in shared HL2 loose files\r\n			game				|all_source_engine_paths|hl2\r\n			platform			|all_source_engine_paths|platform\r\n		}\r\n	}\r\n}\r\n";

            if (!File.Exists(path_final))
            {
                FileStream file_gameinfo = File.Create(path_final);
                file_gameinfo.Close();
            }

            File.WriteAllText(path_final,gameinfo);
        }
		
        private void unreal_gameinfo_modded()
        {
            string path_1 = System.Environment.GetFolderPath(System.Environment.SpecialFolder.ProgramFilesX86);
            string path_2 = @"Steam\SteamApps\common\Half-Life 2\hl2\gameinfo.txt";
            string path_final = Path.Combine(path_1, path_2);
            string gameinfo = "\"GameInfo\"\r\n{\r\n	game 		\"HALF-LIFE 2\"\r\n	title 		\"Unreal Half Life\"\r\n	type		singleplayer_only\r\n	supportsvr	1\r\n\r\n	FileSystem\r\n	{\r\n		SteamAppId				220		// This will mount all the GCFs we need (240=CS:S, 220=HL2).\r\n		\r\n		//\r\n		// The code that loads this file automatically does a few things here:\r\n		//\r\n		// 1. For each \"Game\" search path, it adds a \"GameBin\" path, in <dir>\\bin\r\n		// 2. For each \"Game\" search path, it adds another \"Game\" path in front of it with _<langage> at the end.\r\n		//    For example: c:\\hl2\\cstrike on a french machine would get a c:\\hl2\\cstrike_french path added to it.\r\n		// 3. For the first \"Game\" search path, it adds a search path called \"MOD\".\r\n		// 4. For the first \"Game\" search path, it adds a search path called \"DEFAULT_WRITE_PATH\".\r\n		//\r\n\r\n		//\r\n		// Search paths are relative to the base directory, which is where hl2.exe is found.\r\n		//\r\n		// |gameinfo_path| points at the directory where gameinfo.txt is.\r\n		// We always want to mount that directory relative to gameinfo.txt, so\r\n		// people can mount stuff in c:\\mymod, and the main game resources are in\r\n		// someplace like c:\\program files\\valve\\steam\\steamapps\\half-life 2.\r\n		//\r\n		SearchPaths\r\n		{\r\n			// First, mount all user customizations.  This will search for VPKs and subfolders\r\n			// and mount them in alphabetical order.  The easiest way to distribute a mod is to\r\n			// pack up the custom content into a VPK.  To \"install\" a mod, just drop it in this\r\n			// folder.\r\n			//\r\n			// Note that this folder is scanned only when the game is booted.\r\n			game+mod			hl2/unreal/_Assets/*\r\n\r\n			// We search VPK files before ordinary folders, because most files will be found in\r\n			// VPK and we can avoid making thousands of file system calls to attempt to open files\r\n			// in folders where they don\'t exist.  (Searching a VPK is much faster than making an operating\r\n			// system call.)\r\n			game_lv				hl2/hl2_lv.vpk\r\n			game+mod			hl2/hl2_sound_vo_english.vpk\r\n			game+mod			hl2/hl2_pak.vpk\r\n			game				|all_source_engine_paths|hl2/hl2_textures.vpk\r\n			game				|all_source_engine_paths|hl2/hl2_sound_misc.vpk\r\n			game				|all_source_engine_paths|hl2/hl2_misc.vpk\r\n			platform			|all_source_engine_paths|platform/platform_misc.vpk\r\n\r\n			// Now search loose files.  We\'ll set the directory containing the gameinfo.txt file\r\n			// as the first \"mod\" search path (after any user customizations).  This is also the one\r\n			// that\'s used when writing to the \"mod\" path.\r\n			mod+mod_write+default_write_path		|gameinfo_path|.\r\n\r\n			// Add the HL2 directory as a game search path.  This is also where where writes\r\n			// to the \"game\" path go.\r\n			game+game_write		hl2\r\n\r\n			// Where the game\'s binaries are\r\n			gamebin				hl2/bin\r\n\r\n			// Last, mount in shared HL2 loose files\r\n			game				|all_source_engine_paths|hl2\r\n			platform			|all_source_engine_paths|platform\r\n		}\r\n	}\r\n}\r\n";

            if (!File.Exists(path_final))
            {
                FileStream file_gameinfo = File.Create(path_final);
                file_gameinfo.Close();
            }

            File.WriteAllText(path_final, gameinfo);
        }
		
        private void unreal_gamesounds_normal()
        {
            string path_1 = System.Environment.GetFolderPath(System.Environment.SpecialFolder.ProgramFilesX86);
            string path_2 = @"Steam\SteamApps\common\Half-Life 2\hl2\scripts\game_sounds_manifest.txt";
            string path_final = Path.Combine(path_1, path_2);
            string gamesounds = "game_sounds_manifest\r\n{\r\n	\"precache_file\"		\"scripts/game_sounds.txt\"\r\n	\"precache_file\"		\"scripts/game_sounds_ui.txt\"\r\n	\"precache_file\"		\"scripts/game_sounds_player.txt\"\r\n\r\n	// Weapon sounds\r\n	\"precache_file\"		\"scripts/game_sounds_weapons.txt\"\r\n\r\n	// HL2 World, Ambient Generic, Items, Physics, Vehicles\r\n	\"precache_file\"		\"scripts/game_sounds_world.txt\"\r\n	\"precache_file\"		\"scripts/game_sounds_ambient_generic.txt\"\r\n	\"precache_file\"		\"scripts/game_sounds_items.txt\"\r\n	\"precache_file\"		\"scripts/game_sounds_physics.txt\"\r\n	\"precache_file\"		\"scripts/game_sounds_vehicles.txt\"\r\n\r\n	// E3 level sounds\r\n	\"precache_file\"		\"scripts/level_sounds_e3_c17.txt\"\r\n	\"precache_file\"		\"scripts/level_sounds_e3_town.txt\"\r\n	\"precache_file\"		\"scripts/level_sounds_e3_bugbait.txt\"\r\n\r\n	// Game level sounds\r\n	\"precache_file\"		\"scripts/level_sounds_eli_lab.txt\"\r\n	\"precache_file\"		\"scripts/level_sounds_trainyard.txt\"\r\n	\"precache_file\"		\"scripts/level_sounds_k_lab.txt\"\r\n	\"precache_file\"		\"scripts/level_sounds_k_lab2.txt\"\r\n	\"precache_file\"		\"scripts/level_sounds_coast.txt\"\r\n	\"precache_file\"		\"scripts/level_sounds_novaprospekt.txt\"\r\n	\"precache_file\"		\"scripts/level_sounds_streetwar.txt\"\r\n	\"precache_file\"		\"scripts/level_sounds_streetwar2.txt\"\r\n	\"precache_file\"		\"scripts/level_sounds_breencast.txt\"\r\n	\"precache_file\"		\"scripts/level_sounds_citadel.txt\"\r\n	\"precache_file\"		\"scripts/level_sounds_canals.txt\"\r\n	\"precache_file\"		\"scripts/level_sounds_ravenholm.txt\"\r\n	\"precache_file\"		\"scripts/level_sounds_ravenholm2.txt\"\r\n	\"precache_file\"		\"scripts/level_sounds_canals2.txt\"\r\n	//Music Tracks\r\n	\"precache_file\"		\"scripts/level_sounds_music.txt\"\r\n\r\n\r\n	// NPC Sounds\r\n	\"precache_file\"		\"scripts/npc_sounds_eli.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_alyx.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_dog.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_citizen.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_barney.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_soldier.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_strider.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_zombie.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_vortigaunt.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_turret.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_scanner.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_rollermine.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_poisonzombie.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_metropolice.txt\"\r\n   	\"precache_file\"		\"scripts/npc_sounds_combinecamera.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_manhack.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_ichthyosaur.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_blackheadcrab.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_fastheadcrab.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_headcrab.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_fastzombie.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_birds.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_gunship.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_dropship.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_barnacle.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_attackheli.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_antlionguard.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_antlion.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_env_headcrabcanister.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_combine_ball.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_combine_mine.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_sniper.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_stalker.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_gman.txt\"\r\n}";

            if (!File.Exists(path_final))
            {
                FileStream file_gamesounds = File.Create(path_final);
                file_gamesounds.Close();
            }

            File.WriteAllText(path_final, gamesounds);
        }
		
        private void unreal_gamesounds_modded()
        {
            string path_1 = System.Environment.GetFolderPath(System.Environment.SpecialFolder.ProgramFilesX86);
            string path_2 = @"Steam\SteamApps\common\Half-Life 2\hl2\scripts\game_sounds_manifest.txt";
            string path_final = Path.Combine(path_1, path_2);
            string gamesounds = "game_sounds_manifest\r\n{\r\n	\"precache_file\"		\"scripts/game_sounds.txt\"\r\n	\"precache_file\"		\"scripts/game_sounds_ui.txt\"\r\n	\"precache_file\"		\"scripts/game_sounds_player.txt\"\r\n\r\n	// Weapon sounds\r\n	\"precache_file\"		\"scripts/game_sounds_weapons.txt\"\r\n\r\n	// HL2 World, Ambient Generic, Items, Physics, Vehicles\r\n	\"precache_file\"		\"scripts/game_sounds_world.txt\"\r\n	\"precache_file\"		\"scripts/game_sounds_ambient_generic.txt\"\r\n	\"precache_file\"		\"scripts/game_sounds_items.txt\"\r\n	\"precache_file\"		\"scripts/game_sounds_physics.txt\"\r\n	\"precache_file\"		\"scripts/game_sounds_vehicles.txt\"\r\n\r\n	// E3 level sounds\r\n	\"precache_file\"		\"scripts/level_sounds_e3_c17.txt\"\r\n	\"precache_file\"		\"scripts/level_sounds_e3_town.txt\"\r\n	\"precache_file\"		\"scripts/level_sounds_e3_bugbait.txt\"\r\n\r\n	// Game level sounds\r\n	\"precache_file\"		\"scripts/level_sounds_eli_lab.txt\"\r\n	\"precache_file\"		\"scripts/level_sounds_trainyard.txt\"\r\n	\"precache_file\"		\"scripts/level_sounds_k_lab.txt\"\r\n	\"precache_file\"		\"scripts/level_sounds_k_lab2.txt\"\r\n	\"precache_file\"		\"scripts/level_sounds_coast.txt\"\r\n	\"precache_file\"		\"scripts/level_sounds_novaprospekt.txt\"\r\n	\"precache_file\"		\"scripts/level_sounds_streetwar.txt\"\r\n	\"precache_file\"		\"scripts/level_sounds_streetwar2.txt\"\r\n	\"precache_file\"		\"scripts/level_sounds_breencast.txt\"\r\n	\"precache_file\"		\"scripts/level_sounds_citadel.txt\"\r\n	\"precache_file\"		\"scripts/level_sounds_canals.txt\"\r\n	\"precache_file\"		\"scripts/level_sounds_ravenholm.txt\"\r\n	\"precache_file\"		\"scripts/level_sounds_ravenholm2.txt\"\r\n	\"precache_file\"		\"scripts/level_sounds_canals2.txt\"\r\n	//Music Tracks\r\n	\"precache_file\"		\"scripts/level_sounds_music.txt\"\r\n\r\n\r\n	// NPC Sounds\r\n	\"precache_file\"		\"scripts/npc_sounds_eli.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_alyx.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_dog.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_citizen.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_barney.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_soldier.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_strider.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_zombie.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_vortigaunt.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_turret.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_scanner.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_rollermine.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_poisonzombie.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_metropolice.txt\"\r\n   	\"precache_file\"		\"scripts/npc_sounds_combinecamera.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_manhack.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_ichthyosaur.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_blackheadcrab.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_fastheadcrab.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_headcrab.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_fastzombie.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_birds.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_gunship.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_dropship.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_barnacle.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_attackheli.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_antlionguard.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_antlion.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_env_headcrabcanister.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_combine_ball.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_combine_mine.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_sniper.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_stalker.txt\"\r\n	\"precache_file\"		\"scripts/npc_sounds_gman.txt\"\r\n\r\n	// Unreal\r\n	\"precache_file\"		\"scripts/game_sounds_unreal_ambient.txt\"\r\n	\"precache_file\"		\"scripts/game_sounds_unreal_animals.txt\"\r\n	\"precache_file\"		\"scripts/game_sounds_unreal_music.txt\"\r\n	\"precache_file\"		\"scripts/game_sounds_unreal_portal.txt\"\r\n	\"precache_file\"		\"scripts/game_sounds_unreal_radio.txt\"\r\n	\"precache_file\"		\"scripts/game_sounds_unreal_vo.txt\"\r\n	\"precache_file\"		\"scripts/game_sounds_unreal_weapons.txt\"\r\n}";

            if (!File.Exists(path_final))
            {
                FileStream file_gamesounds = File.Create(path_final);
                file_gamesounds.Close();
            }

            File.WriteAllText(path_final, gamesounds);
        }
		
        private void unreal_gameui_normal()
        {
            string path_1 = System.Environment.GetFolderPath(System.Environment.SpecialFolder.ProgramFilesX86);
            string path_2 = @"Steam\SteamApps\common\Half-Life 2\hl2\resource\hl2_english.txt";
            string path_final = Path.Combine(path_1, path_2);
            string gameui = "\"lang\" \r\n{ \r\n\"Language\" \"English\" \r\n\"Tokens\" \r\n{ \r\n\"HL2_Chapter1_Title\"		\"POINT INSERTION\"\r\n\"HL2_Chapter2_Title\"		\"\\\"A RED LETTER DAY\\\"\"\r\n\"HL2_Chapter3_Title\"		\"ROUTE KANAL\"\r\n\"HL2_Chapter4_Title\"		\"WATER HAZARD\"\r\n\"HL2_Chapter5_Title\"		\"BLACK MESA EAST\"\r\n\"HL2_Chapter6_Title\"		\"\\\"WE DON\'T GO TO RAVENHOLM...\\\"\"\r\n\"HL2_Chapter7_Title\"		\"HIGHWAY 17\"\r\n\"HL2_Chapter8_Title\"		\"SANDTRAPS\"\r\n\"HL2_Chapter9_Title\"		\"NOVA PROSPEKT\"\r\n\"HL2_Chapter9a_Title\"		\"ENTANGLEMENT\"\r\n\"HL2_Chapter10_Title\"		\"ANTICITIZEN ONE\"\r\n\"HL2_Chapter11_Title\"		\"\\\"FOLLOW FREEMAN!\\\"\"\r\n\"HL2_Chapter12_Title\"		\"OUR BENEFACTORS\"\r\n\"HL2_Chapter13_Title\"		\"DARK ENERGY\"\r\n\"HL2_Chapter14_Title\"		\"CREDITS\"\r\n\r\n\"hl2_AmmoFull\"			\"FULL\"\r\n\r\n\"HL2_GameOver_Object\"			\"ASSIGNMENT: TERMINATED\\nSUBJECT: FREEMAN\\nREASON: FAILURE TO PRESERVE MISSION-CRITICAL RESOURCES\"\r\n\r\n\"HL2_GameOver_Ally\"			\"ASSIGNMENT: TERMINATED\\nSUBJECT: FREEMAN\\nREASON: FAILURE TO PRESERVE MISSION-CRITICAL PERSONNEL\"\r\n\r\n\"HL2_GameOver_Timer\"			\"ASSIGNMENT: TERMINATED\\nSUBJECT: FREEMAN\\nREASON: FAILURE TO PREVENT TIME-CRITICAL SEQUENCE\"\r\n\r\n\"HL2_GameOver_Stuck\"			\"ASSIGNMENT: TERMINATED\\nSUBJECT: FREEMAN\\nREASON: DEMONSTRATION OF EXCEEDINGLY POOR JUDGMENT\"\r\n\r\n\"HL2_357Handgun\"	\".357 MAGNUM\"\r\n\"HL2_Pulse_Rifle\"	\"OVERWATCH STANDARD ISSUE\\n(PULSE-RIFLE)\"\r\n\"HL2_Bugbait\"		\"PHEROPOD\\n(BUGBAIT)\"\r\n\"HL2_Crossbow\"		\"CROSSBOW\"\r\n\"HL2_Crowbar\"		\"CROWBAR\"\r\n\"HL2_Grenade\"		\"GRENADE\"\r\n\"HL2_GravityGun\"	\"ZERO-POINT ENERGY GUN\\n(GRAVITY GUN)\"\r\n\"HL2_Pistol\"		\"9MM PISTOL\"\r\n\"HL2_RPG\"		\"RPG\\n(ROCKET PROPELLED GRENADE)\"\r\n\"HL2_Shotgun\"		\"SHOTGUN\"\r\n\"HL2_SMG1\"		\"SMG\\n(SUBMACHINE GUN)\"\r\n\r\n\"HL2_Saved\"		\"Saved...\"\r\n\r\n\"HL2_Credits_VoicesTitle\"		\"Voices:\"\r\n\"HL2_Credits_Eli\"			\"Robert Guillaume - Dr. Eli Vance\"\r\n\"HL2_Credits_Breen\"			\"Robert Culp - Dr. Wallace Breen\"\r\n\"HL2_Credits_Vortigaunt\"		\"Lou Gossett, Jr. - Vortigaunt\"\r\n\"HL2_Credits_Mossman\"			\"Michelle Forbes - Dr. Judith Mossman\"\r\n\"HL2_Credits_Alyx\"			\"Merle Dandridge - Alyx Vance\"\r\n\"HL2_Credits_Barney\"			\"Mike Shapiro - Barney Calhoun\"\r\n\"HL2_Credits_Gman\"			\"Mike Shapiro - Gman\"\r\n\"HL2_Credits_Kleiner\"			\"Harry S. Robins - Dr. Isaac Kleiner\"\r\n\"HL2_Credits_Grigori\"			\"Jim French - Father Grigori\"\r\n\"HL2_Credits_Misc1\"			\"John Patrick Lowrie - Citizens\\Misc. characters\"\r\n\"HL2_Credits_Misc2\"			\"Mary Kae Irvin - Citizens\\Misc. characters\"\r\n\"HL2_Credits_Overwatch\"			\"Ellen McLain - Overwatch\"\r\n\r\n\"HL2_Credits_VoiceCastingTitle\"		\"Voice Casting:\"\r\n\"HL2_Credits_VoiceCastingText\"		\"Shana Landsburg\\Teri Fiddleman\"\r\n\r\n\"HL2_Credits_VoiceRecordingTitle\"	\"Voice Recording:\"\r\n\"HL2_Credits_VoiceRecordingText1\"	\"Pure Audio, Seattle, WA\"\r\n\"HL2_Credits_VoiceRecordingText2\"	\"LA Studios, LA, CA\"\r\n\r\n\"HL2_Credits_VoiceSchedulingTitle\"	\"Voice recording scheduling and logistics:\"\r\n\"HL2_Credits_VoiceSchedulingText\"	\"Pat Cockburn, Pure Audio\"\r\n\r\n\"HL2_Credits_LegalTeam\"			\"Crack Legal Team:\"\r\n\"HL2_Credits_FacesThanks\"		\"Thanks to the following for the use of their faces:\"\r\n\"HL2_Credits_SpecialThanks\"		\"Special thanks to everyone at:\"\r\n\r\n\"HL2_HIT_CANCOP_WITHCAN_NAME\"		\"Defiant\"\r\n\"HL2_HIT_CANCOP_WITHCAN_DESC\"		\"Hit the trashcan cop with the can.\"\r\n\"HL2_PUT_CANINTRASH_NAME\"		\"Submissive\"\r\n\"HL2_PUT_CANINTRASH_DESC\"		\"Put the can in the trash.\"\r\n\"HL2_ESCAPE_APARTMENTRAID_NAME\"		\"Malcontent\"\r\n\"HL2_ESCAPE_APARTMENTRAID_DESC\"		\"Escape the apartment block raid.\"\r\n\"HL2_BREAK_MINITELEPORTER_NAME\"		\"What cat?\"\r\n\"HL2_BREAK_MINITELEPORTER_DESC\"		\"Break the mini-teleporter in Kleiner\'s lab.\"\r\n\"HL2_GET_CROWBAR_NAME\"			\"Trusty Hardware\"\r\n\"HL2_GET_CROWBAR_DESC\"			\"Get the crowbar.\"\r\n\"HL2_KILL_BARNACLESWITHBARREL_NAME\"	\"Barnacle Bowling\"\r\n\"HL2_KILL_BARNACLESWITHBARREL_DESC\"	\"Kill five barnacles with one barrel.\"\r\n\"HL2_GET_AIRBOAT_NAME\"			\"Anchor\'s Aweigh!\"\r\n\"HL2_GET_AIRBOAT_DESC\"			\"Get the airboat.\"\r\n\"HL2_FLOAT_WITHAIRBOAT_NAME\"		\"Catching Air\"\r\n\"HL2_FLOAT_WITHAIRBOAT_DESC\"		\"Float five seconds in the air with the airboat.\"\r\n\"HL2_GET_AIRBOATGUN_NAME\"		\"Heavy Weapons\"\r\n\"HL2_GET_AIRBOATGUN_DESC\"		\"Get the airboat\'s mounted gun.\"\r\n\"HL2_FIND_VORTIGAUNTCAVE_NAME\"		\"Vorticough\"\r\n\"HL2_FIND_VORTIGAUNTCAVE_DESC\"		\"Discover the hidden singing vortigaunt cave in chapter Water Hazard.\"\r\n\"HL2_KILL_CHOPPER_NAME\"			\"Revenge!\"\r\n\"HL2_KILL_CHOPPER_DESC\"			\"Destroy the hunter-chopper in Half-Life 2.\"\r\n\"HL2_FIND_HEVFACEPLATE_NAME\"		\"Blast from the Past\"\r\n\"HL2_FIND_HEVFACEPLATE_DESC\"		\"Find the HEV Suit Charger faceplate in Eli\'s scrapyard.\"\r\n\"HL2_GET_GRAVITYGUN_NAME\"		\"Zero-Point Energy\"\r\n\"HL2_GET_GRAVITYGUN_DESC\"		\"Get the Gravity Gun in Black Mesa East.\"\r\n\"HL2_MAKEABASKET_NAME\"			\"Two Points\"\r\n\"HL2_MAKEABASKET_DESC\"			\"Use DOG\'s ball to make a basket in Eli\'s scrapyard.\"\r\n\"HL2_BEAT_RAVENHOLM_NOWEAPONS_NAME\"	\"Zombie Chopper\"\r\n\"HL2_BEAT_RAVENHOLM_NOWEAPONS_DESC\"	\"Play through Ravenholm using only the Gravity Gun.\"\r\n\"HL2_BEAT_CEMETERY_NAME\"		\"Hallowed Ground\"\r\n\"HL2_BEAT_CEMETERY_DESC\"		\"Escort Grigori safely through the church cemetery.\"\r\n\"HL2_KILL_ENEMIES_WITHCRANE_NAME\"	\"OSHA Violation\"\r\n\"HL2_KILL_ENEMIES_WITHCRANE_DESC\"	\"Kill 3 enemies using the crane.\"\r\n\"HL2_PIN_SOLDIER_TOBILLBOARD_NAME\"	\"Targetted Advertising\"\r\n\"HL2_PIN_SOLDIER_TOBILLBOARD_DESC\"	\"Pin a soldier to the billboard in chapter Highway 17.\"\r\n\"HL2_KILL_ODESSAGUNSHIP_NAME\"		\"Where Cubbage Fears to Tread\"\r\n\"HL2_KILL_ODESSAGUNSHIP_DESC\"		\"Defend Little Odessa from the gunship attack.\"\r\n\"HL2_KILL_THREEGUNSHIPS_NAME\"		\"One Man Army\"\r\n\"HL2_KILL_THREEGUNSHIPS_DESC\"		\"Destroy six gunships in Half-Life 2.\"\r\n\"HL2_BEAT_DONTTOUCHSAND_NAME\"		\"Keep Off the Sand!\"\r\n\"HL2_BEAT_DONTTOUCHSAND_DESC\"		\"Cross the antlion beach in chapter Sandtraps without touching the sand.\"\r\n\"HL2_KILL_BOTHPRISONGUNSHIPS_NAME\"	\"Uninvited Guest\"\r\n\"HL2_KILL_BOTHPRISONGUNSHIPS_DESC\"	\"Kill both gunships in the Nova Prospekt courtyard.\"\r\n\"HL2_KILL_ENEMIES_WITHANTLIONS_NAME\"	\"Bug Hunt\"\r\n\"HL2_KILL_ENEMIES_WITHANTLIONS_DESC\"	\"Use the antlions to kill 50 enemies.\"\r\n\"HL2_KILL_ENEMY_WITHTOILET_NAME\"	\"Flushed\"\r\n\"HL2_KILL_ENEMY_WITHTOILET_DESC\"	\"Kill an enemy with a toilet.\"\r\n\"HL2_BEAT_TURRETSTANDOFF2_NAME\"		\"Warden Freeman\"\r\n\"HL2_BEAT_TURRETSTANDOFF2_DESC\"		\"Survive the second turret standoff in Nova Prospekt.\"\r\n\"HL2_FOLLOWFREEMAN_NAME\"		\"Follow Freeman\"\r\n\"HL2_FOLLOWFREEMAN_DESC\"		\"Gain command of a squad of rebels in the uprising.\"\r\n\"HL2_BEAT_TOXICTUNNEL_NAME\"		\"Radiation Levels Detected\"\r\n\"HL2_BEAT_TOXICTUNNEL_DESC\"		\"Get through the toxic tunnel under City 17 in Half-Life 2.\"\r\n\"HL2_BEAT_PLAZASTANDOFF_NAME\"		\"Plaza Defender\"\r\n\"HL2_BEAT_PLAZASTANDOFF_DESC\"		\"Survive the generator plaza standoff in chapter Anticitizen One.\"\r\n\"HL2_KILL_ALLC1709SNIPERS_NAME\"		\"Counter-Sniper\"\r\n\"HL2_KILL_ALLC1709SNIPERS_DESC\"		\"Kill all of the snipers in City 17.\"\r\n\"HL2_BEAT_SUPRESSIONDEVICE_NAME\"	\"Fight the Power\"\r\n\"HL2_BEAT_SUPRESSIONDEVICE_DESC\"	\"Shut down the supression device by disabling its generators.\"\r\n\"HL2_BEAT_C1713STRIDERSTANDOFF_NAME\"	\"Giant Killer\"\r\n\"HL2_BEAT_C1713STRIDERSTANDOFF_DESC\"	\"Survive the rooftop strider battle in the ruins of City 17.\"\r\n\"HL2_DISINTEGRATE_SOLDIERSINFIELD_NAME\"	\"Atomizer\"\r\n\"HL2_DISINTEGRATE_SOLDIERSINFIELD_DESC\"	\"Disintegrate 15 soldiers by throwing them into a Combine ball field.\"\r\n\"HL2_BEAT_GAME_NAME\"			\"Singularity Collapse\"\r\n\"HL2_BEAT_GAME_DESC\"			\"Destroy the Citadel\'s reactor core.\"\r\n\"HL2_FIND_ALLLAMBDAS_NAME\"		\"Lambda Locator\"\r\n\"HL2_FIND_ALLLAMBDAS_DESC\"		\"Find all lambda caches in Half-Life 2.\"\r\n} \r\n}\r\n";

            if (!File.Exists(path_final))
            {
                FileStream file_gameui = File.Create(path_final);
                file_gameui.Close();
            }

            File.WriteAllText(path_final, gameui, Encoding.Unicode);
        }
		
        private void unreal_gameui_modded()
        {
            string path_1 = System.Environment.GetFolderPath(System.Environment.SpecialFolder.ProgramFilesX86);
            string path_2 = @"Steam\SteamApps\common\Half-Life 2\hl2\resource\hl2_english.txt";
            string path_final = Path.Combine(path_1, path_2);
            string gameui = "\"lang\" \r\n{ \r\n\"Language\" \"English\" \r\n\"Tokens\" \r\n{ \r\n\"HL2_Chapter1_Title\"		\"FORGOTTEN FOREST\"\r\n\"HL2_Chapter2_Title\"		\"CHURCH OF FREEMAN\"\r\n\"HL2_Chapter3_Title\"		\"FOREIGN ABDUCTION\"\r\n\"HL2_Chapter4_Title\"		\"HAUNTED WASTELAND\"\r\n\"HL2_Chapter5_Title\"		\"DESERT TEMPLE\"\r\n\"HL2_Chapter6_Title\"		\"DEEP DESERT\"\r\n\"HL2_Chapter7_Title\"		\"APERTURE SCIENCE\"\r\n\"HL2_Chapter8_Title\"		\"CREDITS\"\r\n\r\n\"hl2_AmmoFull\"			\"FULL\"\r\n\r\n\"HL2_GameOver_Object\"			\"ASSIGNMENT: TERMINATED\\nSUBJECT: FREEMAN\\nREASON: FAILURE TO PRESERVE MISSION-CRITICAL RESOURCES\"\r\n\r\n\"HL2_GameOver_Ally\"			\"ASSIGNMENT: TERMINATED\\nSUBJECT: FREEMAN\\nREASON: FAILURE TO PRESERVE MISSION-CRITICAL PERSONNEL\"\r\n\r\n\"HL2_GameOver_Timer\"			\"ASSIGNMENT: TERMINATED\\nSUBJECT: FREEMAN\\nREASON: FAILURE TO PREVENT TIME-CRITICAL SEQUENCE\"\r\n\r\n\"HL2_GameOver_Stuck\"			\"ASSIGNMENT: TERMINATED\\nSUBJECT: FREEMAN\\nREASON: DEMONSTRATION OF EXCEEDINGLY POOR JUDGMENT\"\r\n\r\n\"HL2_357Handgun\"	\".357 MAGNUM\"\r\n\"HL2_Pulse_Rifle\"	\"OVERWATCH STANDARD ISSUE\\n(PULSE-RIFLE)\"\r\n\"HL2_Bugbait\"		\"PHEROPOD\\n(BUGBAIT)\"\r\n\"HL2_Crossbow\"		\"CROSSBOW\"\r\n\"HL2_Crowbar\"		\"CROWBAR\"\r\n\"HL2_Grenade\"		\"GRENADE\"\r\n\"HL2_GravityGun\"	\"ZERO-POINT ENERGY GUN\\n(GRAVITY GUN)\"\r\n\"HL2_Pistol\"		\"9MM PISTOL\"\r\n\"HL2_RPG\"		\"RPG\\n(ROCKET PROPELLED GRENADE)\"\r\n\"HL2_Shotgun\"		\"SHOTGUN\"\r\n\"HL2_SMG1\"		\"SMG\\n(SUBMACHINE GUN)\"\r\n\r\n\"HL2_Saved\"		\"Saved...\"\r\n\r\n\"HL2_Credits_VoicesTitle\"		\"Voices:\"\r\n\"HL2_Credits_Eli\"			\"Robert Guillaume - Dr. Eli Vance\"\r\n\"HL2_Credits_Breen\"			\"Robert Culp - Dr. Wallace Breen\"\r\n\"HL2_Credits_Vortigaunt\"		\"Lou Gossett, Jr. - Vortigaunt\"\r\n\"HL2_Credits_Mossman\"			\"Michelle Forbes - Dr. Judith Mossman\"\r\n\"HL2_Credits_Alyx\"			\"Merle Dandridge - Alyx Vance\"\r\n\"HL2_Credits_Barney\"			\"Mike Shapiro - Barney Calhoun\"\r\n\"HL2_Credits_Gman\"			\"Mike Shapiro - Gman\"\r\n\"HL2_Credits_Kleiner\"			\"Harry S. Robins - Dr. Isaac Kleiner\"\r\n\"HL2_Credits_Grigori\"			\"Jim French - Father Grigori\"\r\n\"HL2_Credits_Misc1\"			\"John Patrick Lowrie - Citizens\\Misc. characters\"\r\n\"HL2_Credits_Misc2\"			\"Mary Kae Irvin - Citizens\\Misc. characters\"\r\n\"HL2_Credits_Overwatch\"			\"Ellen McLain - Overwatch\"\r\n\r\n\"HL2_Credits_VoiceCastingTitle\"		\"Voice Casting:\"\r\n\"HL2_Credits_VoiceCastingText\"		\"Shana Landsburg\\Teri Fiddleman\"\r\n\r\n\"HL2_Credits_VoiceRecordingTitle\"	\"Voice Recording:\"\r\n\"HL2_Credits_VoiceRecordingText1\"	\"Pure Audio, Seattle, WA\"\r\n\"HL2_Credits_VoiceRecordingText2\"	\"LA Studios, LA, CA\"\r\n\r\n\"HL2_Credits_VoiceSchedulingTitle\"	\"Voice recording scheduling and logistics:\"\r\n\"HL2_Credits_VoiceSchedulingText\"	\"Pat Cockburn, Pure Audio\"\r\n\r\n\"HL2_Credits_LegalTeam\"			\"Crack Legal Team:\"\r\n\"HL2_Credits_FacesThanks\"		\"Thanks to the following for the use of their faces:\"\r\n\"HL2_Credits_SpecialThanks\"		\"Special thanks to everyone at:\"\r\n\r\n\"HL2_HIT_CANCOP_WITHCAN_NAME\"		\"Defiant\"\r\n\"HL2_HIT_CANCOP_WITHCAN_DESC\"		\"Hit the trashcan cop with the can.\"\r\n\"HL2_PUT_CANINTRASH_NAME\"		\"Submissive\"\r\n\"HL2_PUT_CANINTRASH_DESC\"		\"Put the can in the trash.\"\r\n\"HL2_ESCAPE_APARTMENTRAID_NAME\"		\"Malcontent\"\r\n\"HL2_ESCAPE_APARTMENTRAID_DESC\"		\"Escape the apartment block raid.\"\r\n\"HL2_BREAK_MINITELEPORTER_NAME\"		\"What cat?\"\r\n\"HL2_BREAK_MINITELEPORTER_DESC\"		\"Break the mini-teleporter in Kleiner\'s lab.\"\r\n\"HL2_GET_CROWBAR_NAME\"			\"Trusty Hardware\"\r\n\"HL2_GET_CROWBAR_DESC\"			\"Get the crowbar.\"\r\n\"HL2_KILL_BARNACLESWITHBARREL_NAME\"	\"Barnacle Bowling\"\r\n\"HL2_KILL_BARNACLESWITHBARREL_DESC\"	\"Kill five barnacles with one barrel.\"\r\n\"HL2_GET_AIRBOAT_NAME\"			\"Anchor\'s Aweigh!\"\r\n\"HL2_GET_AIRBOAT_DESC\"			\"Get the airboat.\"\r\n\"HL2_FLOAT_WITHAIRBOAT_NAME\"		\"Catching Air\"\r\n\"HL2_FLOAT_WITHAIRBOAT_DESC\"		\"Float five seconds in the air with the airboat.\"\r\n\"HL2_GET_AIRBOATGUN_NAME\"		\"Heavy Weapons\"\r\n\"HL2_GET_AIRBOATGUN_DESC\"		\"Get the airboat\'s mounted gun.\"\r\n\"HL2_FIND_VORTIGAUNTCAVE_NAME\"		\"Vorticough\"\r\n\"HL2_FIND_VORTIGAUNTCAVE_DESC\"		\"Discover the hidden singing vortigaunt cave in chapter Water Hazard.\"\r\n\"HL2_KILL_CHOPPER_NAME\"			\"Revenge!\"\r\n\"HL2_KILL_CHOPPER_DESC\"			\"Destroy the hunter-chopper in Half-Life 2.\"\r\n\"HL2_FIND_HEVFACEPLATE_NAME\"		\"Blast from the Past\"\r\n\"HL2_FIND_HEVFACEPLATE_DESC\"		\"Find the HEV Suit Charger faceplate in Eli\'s scrapyard.\"\r\n\"HL2_GET_GRAVITYGUN_NAME\"		\"Zero-Point Energy\"\r\n\"HL2_GET_GRAVITYGUN_DESC\"		\"Get the Gravity Gun in Black Mesa East.\"\r\n\"HL2_MAKEABASKET_NAME\"			\"Two Points\"\r\n\"HL2_MAKEABASKET_DESC\"			\"Use DOG\'s ball to make a basket in Eli\'s scrapyard.\"\r\n\"HL2_BEAT_RAVENHOLM_NOWEAPONS_NAME\"	\"Zombie Chopper\"\r\n\"HL2_BEAT_RAVENHOLM_NOWEAPONS_DESC\"	\"Play through Ravenholm using only the Gravity Gun.\"\r\n\"HL2_BEAT_CEMETERY_NAME\"		\"Hallowed Ground\"\r\n\"HL2_BEAT_CEMETERY_DESC\"		\"Escort Grigori safely through the church cemetery.\"\r\n\"HL2_KILL_ENEMIES_WITHCRANE_NAME\"	\"OSHA Violation\"\r\n\"HL2_KILL_ENEMIES_WITHCRANE_DESC\"	\"Kill 3 enemies using the crane.\"\r\n\"HL2_PIN_SOLDIER_TOBILLBOARD_NAME\"	\"Targetted Advertising\"\r\n\"HL2_PIN_SOLDIER_TOBILLBOARD_DESC\"	\"Pin a soldier to the billboard in chapter Highway 17.\"\r\n\"HL2_KILL_ODESSAGUNSHIP_NAME\"		\"Where Cubbage Fears to Tread\"\r\n\"HL2_KILL_ODESSAGUNSHIP_DESC\"		\"Defend Little Odessa from the gunship attack.\"\r\n\"HL2_KILL_THREEGUNSHIPS_NAME\"		\"One Man Army\"\r\n\"HL2_KILL_THREEGUNSHIPS_DESC\"		\"Destroy six gunships in Half-Life 2.\"\r\n\"HL2_BEAT_DONTTOUCHSAND_NAME\"		\"Keep Off the Sand!\"\r\n\"HL2_BEAT_DONTTOUCHSAND_DESC\"		\"Cross the antlion beach in chapter Sandtraps without touching the sand.\"\r\n\"HL2_KILL_BOTHPRISONGUNSHIPS_NAME\"	\"Uninvited Guest\"\r\n\"HL2_KILL_BOTHPRISONGUNSHIPS_DESC\"	\"Kill both gunships in the Nova Prospekt courtyard.\"\r\n\"HL2_KILL_ENEMIES_WITHANTLIONS_NAME\"	\"Bug Hunt\"\r\n\"HL2_KILL_ENEMIES_WITHANTLIONS_DESC\"	\"Use the antlions to kill 50 enemies.\"\r\n\"HL2_KILL_ENEMY_WITHTOILET_NAME\"	\"Flushed\"\r\n\"HL2_KILL_ENEMY_WITHTOILET_DESC\"	\"Kill an enemy with a toilet.\"\r\n\"HL2_BEAT_TURRETSTANDOFF2_NAME\"		\"Warden Freeman\"\r\n\"HL2_BEAT_TURRETSTANDOFF2_DESC\"		\"Survive the second turret standoff in Nova Prospekt.\"\r\n\"HL2_FOLLOWFREEMAN_NAME\"		\"Follow Freeman\"\r\n\"HL2_FOLLOWFREEMAN_DESC\"		\"Gain command of a squad of rebels in the uprising.\"\r\n\"HL2_BEAT_TOXICTUNNEL_NAME\"		\"Radiation Levels Detected\"\r\n\"HL2_BEAT_TOXICTUNNEL_DESC\"		\"Get through the toxic tunnel under City 17 in Half-Life 2.\"\r\n\"HL2_BEAT_PLAZASTANDOFF_NAME\"		\"Plaza Defender\"\r\n\"HL2_BEAT_PLAZASTANDOFF_DESC\"		\"Survive the generator plaza standoff in chapter Anticitizen One.\"\r\n\"HL2_KILL_ALLC1709SNIPERS_NAME\"		\"Counter-Sniper\"\r\n\"HL2_KILL_ALLC1709SNIPERS_DESC\"		\"Kill all of the snipers in City 17.\"\r\n\"HL2_BEAT_SUPRESSIONDEVICE_NAME\"	\"Fight the Power\"\r\n\"HL2_BEAT_SUPRESSIONDEVICE_DESC\"	\"Shut down the supression device by disabling its generators.\"\r\n\"HL2_BEAT_C1713STRIDERSTANDOFF_NAME\"	\"Giant Killer\"\r\n\"HL2_BEAT_C1713STRIDERSTANDOFF_DESC\"	\"Survive the rooftop strider battle in the ruins of City 17.\"\r\n\"HL2_DISINTEGRATE_SOLDIERSINFIELD_NAME\"	\"Atomizer\"\r\n\"HL2_DISINTEGRATE_SOLDIERSINFIELD_DESC\"	\"Disintegrate 15 soldiers by throwing them into a Combine ball field.\"\r\n\"HL2_BEAT_GAME_NAME\"			\"Singularity Collapse\"\r\n\"HL2_BEAT_GAME_DESC\"			\"Destroy the Citadel\'s reactor core.\"\r\n\"HL2_FIND_ALLLAMBDAS_NAME\"		\"Lambda Locator\"\r\n\"HL2_FIND_ALLLAMBDAS_DESC\"		\"Find all lambda caches in Half-Life 2.\"\r\n} \r\n}\r\n";
 
            if (!File.Exists(path_final))
            {
                FileStream file_gameui = File.Create(path_final);
                file_gameui.Close();
            }

            File.WriteAllText(path_final, gameui, Encoding.Unicode);
        }
		
        private void unreal_gamechapters_normal()
        {
            string[] path_chapters = new string[15];
            string[] path_contents = new string[15];

            string path_main = System.Environment.GetFolderPath(System.Environment.SpecialFolder.ProgramFilesX86);
            string path_chapter1 = @"Steam\SteamApps\common\Half-Life 2\hl2\cfg\chapter1.cfg";
            string path_chapter2 = @"Steam\SteamApps\common\Half-Life 2\hl2\cfg\chapter2.cfg";
            string path_chapter3 = @"Steam\SteamApps\common\Half-Life 2\hl2\cfg\chapter3.cfg";
            string path_chapter4 = @"Steam\SteamApps\common\Half-Life 2\hl2\cfg\chapter4.cfg";
            string path_chapter5 = @"Steam\SteamApps\common\Half-Life 2\hl2\cfg\chapter5.cfg";
            string path_chapter6 = @"Steam\SteamApps\common\Half-Life 2\hl2\cfg\chapter6.cfg";
            string path_chapter7 = @"Steam\SteamApps\common\Half-Life 2\hl2\cfg\chapter7.cfg";
            string path_chapter8 = @"Steam\SteamApps\common\Half-Life 2\hl2\cfg\chapter8.cfg";
            string path_chapter9 = @"Steam\SteamApps\common\Half-Life 2\hl2\cfg\chapter9.cfg";
            string path_chapter9a = @"Steam\SteamApps\common\Half-Life 2\hl2\cfg\chapter9a.cfg";
            string path_chapter10 = @"Steam\SteamApps\common\Half-Life 2\hl2\cfg\chapter10.cfg";
            string path_chapter11 = @"Steam\SteamApps\common\Half-Life 2\hl2\cfg\chapter11.cfg";
            string path_chapter12 = @"Steam\SteamApps\common\Half-Life 2\hl2\cfg\chapter12.cfg";
            string path_chapter13 = @"Steam\SteamApps\common\Half-Life 2\hl2\cfg\chapter13.cfg";
            string path_chapter14 = @"Steam\SteamApps\common\Half-Life 2\hl2\cfg\chapter14.cfg";

            path_chapters[0] = Path.Combine(path_main, path_chapter1);
            path_chapters[1] = Path.Combine(path_main, path_chapter2);
            path_chapters[2] = Path.Combine(path_main, path_chapter3);
            path_chapters[3] = Path.Combine(path_main, path_chapter4);
            path_chapters[4] = Path.Combine(path_main, path_chapter5);
            path_chapters[5] = Path.Combine(path_main, path_chapter6);
            path_chapters[6] = Path.Combine(path_main, path_chapter7);
            path_chapters[7] = Path.Combine(path_main, path_chapter8);
            path_chapters[8] = Path.Combine(path_main, path_chapter9);
            path_chapters[9] = Path.Combine(path_main, path_chapter9a);
            path_chapters[10] = Path.Combine(path_main, path_chapter10);
            path_chapters[11] = Path.Combine(path_main, path_chapter11);
            path_chapters[12] = Path.Combine(path_main, path_chapter12);
            path_chapters[13] = Path.Combine(path_main, path_chapter13);
            path_chapters[14] = Path.Combine(path_main, path_chapter14);

            path_contents[0] = "map d1_trainstation_01";
            path_contents[1] = "map d1_trainstation_05";
            path_contents[2] = "map d1_canals_01";
            path_contents[3] = "map d1_canals_06";
            path_contents[4] = "map d1_eli_01";
            path_contents[5] = "map d1_town_01";
            path_contents[6] = "map d2_coast_01";
            path_contents[7] = "map d2_coast_09";
            path_contents[8] = "map d2_prison_02";
            path_contents[9] = "map d2_prison_06";
            path_contents[10] = "map d3_c17_02";
            path_contents[11] = "map d3_c17_09";
            path_contents[12] = "map d3_citadel_01";
            path_contents[13] = "map d3_breen_01";
            path_contents[14] = "map credits";

            for (int i = 0; i < path_chapters.Length; i++)
            {
                if (!File.Exists(path_chapters[i]))
                {
                    FileStream file_chapters = File.Create(path_chapters[i]);
                    file_chapters.Close();
                }
            }

            for (int i = 0; i < path_chapters.Length; i++)
            {
                File.WriteAllText(path_chapters[i], path_contents[i]);
            }
        }
		
        private void unreal_gamechapters_modded()
        {
            string[] path_chapters = new string[15];

            string path_main = System.Environment.GetFolderPath(System.Environment.SpecialFolder.ProgramFilesX86);
            string path_chapter1 = @"Steam\SteamApps\common\Half-Life 2\hl2\cfg\chapter1.cfg";
            string path_chapter2 = @"Steam\SteamApps\common\Half-Life 2\hl2\cfg\chapter2.cfg";
            string path_chapter3 = @"Steam\SteamApps\common\Half-Life 2\hl2\cfg\chapter3.cfg";
            string path_chapter4 = @"Steam\SteamApps\common\Half-Life 2\hl2\cfg\chapter4.cfg";
            string path_chapter5 = @"Steam\SteamApps\common\Half-Life 2\hl2\cfg\chapter5.cfg";
            string path_chapter6 = @"Steam\SteamApps\common\Half-Life 2\hl2\cfg\chapter6.cfg";
            string path_chapter7 = @"Steam\SteamApps\common\Half-Life 2\hl2\cfg\chapter7.cfg";
            string path_chapter8 = @"Steam\SteamApps\common\Half-Life 2\hl2\cfg\chapter8.cfg";
            string path_chapter9 = @"Steam\SteamApps\common\Half-Life 2\hl2\cfg\chapter9.cfg";
            string path_chapter9a = @"Steam\SteamApps\common\Half-Life 2\hl2\cfg\chapter9a.cfg";
            string path_chapter10 = @"Steam\SteamApps\common\Half-Life 2\hl2\cfg\chapter10.cfg";
            string path_chapter11 = @"Steam\SteamApps\common\Half-Life 2\hl2\cfg\chapter11.cfg";
            string path_chapter12 = @"Steam\SteamApps\common\Half-Life 2\hl2\cfg\chapter12.cfg";
            string path_chapter13 = @"Steam\SteamApps\common\Half-Life 2\hl2\cfg\chapter13.cfg";
            string path_chapter14 = @"Steam\SteamApps\common\Half-Life 2\hl2\cfg\chapter14.cfg";

            path_chapters[0] = Path.Combine(path_main, path_chapter1);
            path_chapters[1] = Path.Combine(path_main, path_chapter2);
            path_chapters[2] = Path.Combine(path_main, path_chapter3);
            path_chapters[3] = Path.Combine(path_main, path_chapter4);
            path_chapters[4] = Path.Combine(path_main, path_chapter5);
            path_chapters[5] = Path.Combine(path_main, path_chapter6);
            path_chapters[6] = Path.Combine(path_main, path_chapter7);
            path_chapters[7] = Path.Combine(path_main, path_chapter8);
            path_chapters[8] = Path.Combine(path_main, path_chapter9);
            path_chapters[9] = Path.Combine(path_main, path_chapter9a);
            path_chapters[10] = Path.Combine(path_main, path_chapter10);
            path_chapters[11] = Path.Combine(path_main, path_chapter11);
            path_chapters[12] = Path.Combine(path_main, path_chapter12);
            path_chapters[13] = Path.Combine(path_main, path_chapter13);
            path_chapters[14] = Path.Combine(path_main, path_chapter14);

            foreach (string path in path_chapters)
            {
                if (File.Exists(path))
                {
                    File.Delete(path);
                }
            }
        }
		
        private void unreal_game_start()
        {
            // Path variables
            string path_1 = System.Environment.GetFolderPath(System.Environment.SpecialFolder.ProgramFilesX86);
            string path_2 = @"Steam\SteamApps\common\Half-Life 2\hl2.exe";
            string path_final = Path.Combine(path_1, path_2);

            // Hide Form
            this.Hide();

            // Edit Files
            unreal_config();
            unreal_gameinfo_modded();
            unreal_gamesounds_modded();
            unreal_gameui_modded();
            unreal_gamechapters_modded();

            // Pause
            System.Threading.Thread.Sleep(1000);

            // Run game
            var process = Process.Start(path_final);
            process.WaitForExit();

            // Pause
            System.Threading.Thread.Sleep(1000);

            // Reset game data
            unreal_gameinfo_normal();
            unreal_gamesounds_normal();
            unreal_gameui_normal();
            unreal_gamechapters_normal();
        }
    }
}
