/********************************
 * Custom Game Show
 * FormMainMenu.Designer.cs
 * Created by Justin Leonard
********************************/

using System.Drawing;

namespace CustomGameShow
{
    partial class FormMainMenu
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(FormMainMenu));
            this.pictureBoxMain = new System.Windows.Forms.PictureBox();
            this.buttonStartGame = new System.Windows.Forms.Button();
            this.buttonSettings = new System.Windows.Forms.Button();
            this.buttonExit = new System.Windows.Forms.Button();
            this.buttonLog = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxMain)).BeginInit();
            this.SuspendLayout();
            // 
            // pictureBoxMain
            // 
            this.pictureBoxMain.BackColor = System.Drawing.SystemColors.Control;
            this.pictureBoxMain.Image = ((System.Drawing.Image)(resources.GetObject("pictureBoxMain.Image")));
            this.pictureBoxMain.Location = new System.Drawing.Point(0, 0);
            this.pictureBoxMain.Name = "pictureBoxMain";
            this.pictureBoxMain.Size = new System.Drawing.Size(1920, 1080);
            this.pictureBoxMain.TabIndex = 0;
            this.pictureBoxMain.TabStop = false;
            // 
            // buttonStartGame
            // 
            this.buttonStartGame.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.buttonStartGame.Font = new System.Drawing.Font("Arial", 36F, System.Drawing.FontStyle.Bold);
            this.buttonStartGame.Image = ((System.Drawing.Image)(resources.GetObject("buttonStartGame.Image")));
            this.buttonStartGame.Location = new System.Drawing.Point(685, 562);
            this.buttonStartGame.Name = "buttonStartGame";
            this.buttonStartGame.Size = new System.Drawing.Size(550, 126);
            this.buttonStartGame.TabIndex = 2;
            this.buttonStartGame.Text = "Start Game";
            this.buttonStartGame.UseVisualStyleBackColor = true;
            this.buttonStartGame.Click += new System.EventHandler(this.buttonStartGame_Click);
            // 
            // buttonSettings
            // 
            this.buttonSettings.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.buttonSettings.Font = new System.Drawing.Font("Arial", 36F, System.Drawing.FontStyle.Bold);
            this.buttonSettings.Image = ((System.Drawing.Image)(resources.GetObject("buttonSettings.Image")));
            this.buttonSettings.Location = new System.Drawing.Point(685, 738);
            this.buttonSettings.Name = "buttonSettings";
            this.buttonSettings.Size = new System.Drawing.Size(250, 126);
            this.buttonSettings.TabIndex = 2;
            this.buttonSettings.Text = "Settings";
            this.buttonSettings.UseVisualStyleBackColor = true;
            this.buttonSettings.Click += new System.EventHandler(this.buttonSettings_Click);
            // 
            // buttonExit
            // 
            this.buttonExit.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.buttonExit.Font = new System.Drawing.Font("Arial", 36F, System.Drawing.FontStyle.Bold);
            this.buttonExit.Image = ((System.Drawing.Image)(resources.GetObject("buttonExit.Image")));
            this.buttonExit.Location = new System.Drawing.Point(685, 914);
            this.buttonExit.Name = "buttonExit";
            this.buttonExit.Size = new System.Drawing.Size(550, 126);
            this.buttonExit.TabIndex = 2;
            this.buttonExit.Text = "Exit";
            this.buttonExit.UseVisualStyleBackColor = true;
            this.buttonExit.Click += new System.EventHandler(this.buttonExit_Click);
            // 
            // buttonLog
            // 
            this.buttonLog.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.buttonLog.Font = new System.Drawing.Font("Arial", 36F, System.Drawing.FontStyle.Bold);
            this.buttonLog.Image = ((System.Drawing.Image)(resources.GetObject("buttonLog.Image")));
            this.buttonLog.Location = new System.Drawing.Point(985, 738);
            this.buttonLog.Name = "buttonLog";
            this.buttonLog.Size = new System.Drawing.Size(250, 126);
            this.buttonLog.TabIndex = 2;
            this.buttonLog.Text = "Log";
            this.buttonLog.UseVisualStyleBackColor = true;
            this.buttonLog.Click += new System.EventHandler(this.buttonLog_Click);
            // 
            // FormMainMenu
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.Control;
            this.ClientSize = new System.Drawing.Size(1920, 1080);
            this.Controls.Add(this.buttonExit);
            this.Controls.Add(this.buttonLog);
            this.Controls.Add(this.buttonSettings);
            this.Controls.Add(this.buttonStartGame);
            this.Controls.Add(this.pictureBoxMain);
            this.Enabled = false;
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "FormMainMenu";
            this.Opacity = 0D;
            this.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Custom Game Show";
            this.Load += new System.EventHandler(this.FormMainMenu_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxMain)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBoxMain;
        private System.Windows.Forms.Button buttonStartGame;
        private System.Windows.Forms.Button buttonSettings;
        private System.Windows.Forms.Button buttonExit;
        private System.Windows.Forms.Button buttonLog;
    }
}