/********************************
 * Custom Game Show
 * FormScoreView.Designer.cs
 * Created by Justin Leonard
********************************/

namespace CustomGameShow
{
    partial class FormScoreView
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(FormScoreView));
            this.buttonExit = new System.Windows.Forms.Button();
            this.labelTitle = new System.Windows.Forms.Label();
            this.labelScore0 = new System.Windows.Forms.Label();
            this.labelScore1 = new System.Windows.Forms.Label();
            this.labelScore2 = new System.Windows.Forms.Label();
            this.labelRound = new System.Windows.Forms.Label();
            this.labelCounter = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // buttonExit
            // 
            this.buttonExit.BackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonExit.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("buttonExit.BackgroundImage")));
            this.buttonExit.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.buttonExit.Cursor = System.Windows.Forms.Cursors.Hand;
            this.buttonExit.FlatAppearance.BorderColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonExit.FlatAppearance.BorderSize = 0;
            this.buttonExit.FlatAppearance.MouseDownBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonExit.FlatAppearance.MouseOverBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonExit.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonExit.Font = new System.Drawing.Font("Arial", 36F, System.Drawing.FontStyle.Bold);
            this.buttonExit.Location = new System.Drawing.Point(91, 469);
            this.buttonExit.Name = "buttonExit";
            this.buttonExit.Size = new System.Drawing.Size(468, 75);
            this.buttonExit.TabIndex = 0;
            this.buttonExit.TabStop = false;
            this.buttonExit.Text = "Exit";
            this.buttonExit.UseVisualStyleBackColor = false;
            this.buttonExit.Click += new System.EventHandler(this.buttonExit_Click);
            // 
            // labelTitle
            // 
            this.labelTitle.AutoSize = true;
            this.labelTitle.Font = new System.Drawing.Font("Arial Black", 48F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelTitle.ForeColor = System.Drawing.SystemColors.ControlText;
            this.labelTitle.Location = new System.Drawing.Point(110, 6);
            this.labelTitle.Name = "labelTitle";
            this.labelTitle.Size = new System.Drawing.Size(438, 90);
            this.labelTitle.TabIndex = 0;
            this.labelTitle.Text = "View Score";
            // 
            // labelScore0
            // 
            this.labelScore0.AutoSize = true;
            this.labelScore0.Font = new System.Drawing.Font("Arial", 36F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelScore0.Location = new System.Drawing.Point(12, 100);
            this.labelScore0.Name = "labelScore0";
            this.labelScore0.Size = new System.Drawing.Size(187, 56);
            this.labelScore0.TabIndex = 0;
            this.labelScore0.Text = "Default";
            // 
            // labelScore1
            // 
            this.labelScore1.AutoSize = true;
            this.labelScore1.Font = new System.Drawing.Font("Arial", 36F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelScore1.Location = new System.Drawing.Point(12, 172);
            this.labelScore1.Name = "labelScore1";
            this.labelScore1.Size = new System.Drawing.Size(187, 56);
            this.labelScore1.TabIndex = 0;
            this.labelScore1.Text = "Default";
            // 
            // labelScore2
            // 
            this.labelScore2.AutoSize = true;
            this.labelScore2.Font = new System.Drawing.Font("Arial", 36F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelScore2.Location = new System.Drawing.Point(12, 244);
            this.labelScore2.Name = "labelScore2";
            this.labelScore2.Size = new System.Drawing.Size(187, 56);
            this.labelScore2.TabIndex = 0;
            this.labelScore2.Text = "Default";
            // 
            // labelRound
            // 
            this.labelRound.AutoSize = true;
            this.labelRound.Font = new System.Drawing.Font("Arial", 36F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelRound.Location = new System.Drawing.Point(12, 388);
            this.labelRound.Name = "labelRound";
            this.labelRound.Size = new System.Drawing.Size(187, 56);
            this.labelRound.TabIndex = 0;
            this.labelRound.Text = "Default";
            // 
            // labelCounter
            // 
            this.labelCounter.AutoSize = true;
            this.labelCounter.Font = new System.Drawing.Font("Arial", 36F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelCounter.Location = new System.Drawing.Point(12, 316);
            this.labelCounter.Name = "labelCounter";
            this.labelCounter.Size = new System.Drawing.Size(187, 56);
            this.labelCounter.TabIndex = 0;
            this.labelCounter.Text = "Default";
            // 
            // FormScoreView
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ScrollBar;
            this.ClientSize = new System.Drawing.Size(650, 572);
            this.Controls.Add(this.labelCounter);
            this.Controls.Add(this.labelRound);
            this.Controls.Add(this.labelScore2);
            this.Controls.Add(this.labelScore1);
            this.Controls.Add(this.labelScore0);
            this.Controls.Add(this.labelTitle);
            this.Controls.Add(this.buttonExit);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.KeyPreview = true;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "FormScoreView";
            this.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Custom Game Show";
            this.Load += new System.EventHandler(this.FormScoreView_Load);
            this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.FormScoreView_KeyDown);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button buttonExit;
        private System.Windows.Forms.Label labelTitle;
        private System.Windows.Forms.Label labelScore0;
        private System.Windows.Forms.Label labelScore1;
        private System.Windows.Forms.Label labelScore2;
        private System.Windows.Forms.Label labelRound;
        private System.Windows.Forms.Label labelCounter;
    }
}