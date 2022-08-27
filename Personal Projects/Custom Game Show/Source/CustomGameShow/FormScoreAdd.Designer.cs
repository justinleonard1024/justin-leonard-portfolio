/********************************
 * Custom Game Show
 * FormScoreAdd.Designer.cs
 * Created by Justin Leonard
********************************/

namespace CustomGameShow
{
    partial class FormScoreAdd
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(FormScoreAdd));
            this.labelTitle = new System.Windows.Forms.Label();
            this.buttonScore0 = new System.Windows.Forms.Button();
            this.buttonScore1 = new System.Windows.Forms.Button();
            this.buttonScore2 = new System.Windows.Forms.Button();
            this.buttonExit = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // labelTitle
            // 
            this.labelTitle.AutoSize = true;
            this.labelTitle.Font = new System.Drawing.Font("Arial Black", 48F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelTitle.ForeColor = System.Drawing.SystemColors.ControlText;
            this.labelTitle.Location = new System.Drawing.Point(76, 30);
            this.labelTitle.Name = "labelTitle";
            this.labelTitle.Size = new System.Drawing.Size(506, 90);
            this.labelTitle.TabIndex = 0;
            this.labelTitle.Text = "Add To Score";
            // 
            // buttonScore0
            // 
            this.buttonScore0.BackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonScore0.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("buttonScore0.BackgroundImage")));
            this.buttonScore0.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.buttonScore0.Cursor = System.Windows.Forms.Cursors.Hand;
            this.buttonScore0.FlatAppearance.BorderColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonScore0.FlatAppearance.BorderSize = 0;
            this.buttonScore0.FlatAppearance.CheckedBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonScore0.FlatAppearance.MouseDownBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonScore0.FlatAppearance.MouseOverBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonScore0.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonScore0.Font = new System.Drawing.Font("Arial", 36F, System.Drawing.FontStyle.Bold);
            this.buttonScore0.Location = new System.Drawing.Point(91, 153);
            this.buttonScore0.Name = "buttonScore0";
            this.buttonScore0.Size = new System.Drawing.Size(468, 75);
            this.buttonScore0.TabIndex = 0;
            this.buttonScore0.TabStop = false;
            this.buttonScore0.Text = "Default";
            this.buttonScore0.UseVisualStyleBackColor = false;
            this.buttonScore0.Click += new System.EventHandler(this.buttonScore_Click);
            // 
            // buttonScore1
            // 
            this.buttonScore1.BackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonScore1.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("buttonScore1.BackgroundImage")));
            this.buttonScore1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.buttonScore1.Cursor = System.Windows.Forms.Cursors.Hand;
            this.buttonScore1.FlatAppearance.BorderColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonScore1.FlatAppearance.BorderSize = 0;
            this.buttonScore1.FlatAppearance.CheckedBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonScore1.FlatAppearance.MouseDownBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonScore1.FlatAppearance.MouseOverBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonScore1.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonScore1.Font = new System.Drawing.Font("Arial", 36F, System.Drawing.FontStyle.Bold);
            this.buttonScore1.Location = new System.Drawing.Point(91, 259);
            this.buttonScore1.Name = "buttonScore1";
            this.buttonScore1.Size = new System.Drawing.Size(468, 75);
            this.buttonScore1.TabIndex = 0;
            this.buttonScore1.TabStop = false;
            this.buttonScore1.Text = "Default";
            this.buttonScore1.UseVisualStyleBackColor = false;
            this.buttonScore1.Click += new System.EventHandler(this.buttonScore_Click);
            // 
            // buttonScore2
            // 
            this.buttonScore2.BackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonScore2.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("buttonScore2.BackgroundImage")));
            this.buttonScore2.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.buttonScore2.Cursor = System.Windows.Forms.Cursors.Hand;
            this.buttonScore2.FlatAppearance.BorderColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonScore2.FlatAppearance.BorderSize = 0;
            this.buttonScore2.FlatAppearance.CheckedBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonScore2.FlatAppearance.MouseDownBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonScore2.FlatAppearance.MouseOverBackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonScore2.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.buttonScore2.Font = new System.Drawing.Font("Arial", 36F, System.Drawing.FontStyle.Bold);
            this.buttonScore2.Location = new System.Drawing.Point(91, 364);
            this.buttonScore2.Name = "buttonScore2";
            this.buttonScore2.Size = new System.Drawing.Size(468, 75);
            this.buttonScore2.TabIndex = 0;
            this.buttonScore2.TabStop = false;
            this.buttonScore2.Text = "Default";
            this.buttonScore2.UseVisualStyleBackColor = false;
            this.buttonScore2.Click += new System.EventHandler(this.buttonScore_Click);
            // 
            // buttonExit
            // 
            this.buttonExit.BackColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonExit.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("buttonExit.BackgroundImage")));
            this.buttonExit.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.buttonExit.Cursor = System.Windows.Forms.Cursors.Hand;
            this.buttonExit.FlatAppearance.BorderColor = System.Drawing.SystemColors.ScrollBar;
            this.buttonExit.FlatAppearance.BorderSize = 0;
            this.buttonExit.FlatAppearance.CheckedBackColor = System.Drawing.SystemColors.ScrollBar;
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
            // FormScoreAdd
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ScrollBar;
            this.ClientSize = new System.Drawing.Size(650, 572);
            this.Controls.Add(this.buttonExit);
            this.Controls.Add(this.buttonScore2);
            this.Controls.Add(this.buttonScore1);
            this.Controls.Add(this.buttonScore0);
            this.Controls.Add(this.labelTitle);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.KeyPreview = true;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "FormScoreAdd";
            this.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Custom Game Show";
            this.Load += new System.EventHandler(this.FormScoreAdd_Load);
            this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.FormScoreAdd_KeyDown);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label labelTitle;
        private System.Windows.Forms.Button buttonScore0;
        private System.Windows.Forms.Button buttonScore1;
        private System.Windows.Forms.Button buttonScore2;
        private System.Windows.Forms.Button buttonExit;
    }
}